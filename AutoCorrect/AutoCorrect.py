import os


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word
    
    
class AutoCorrect:
    def __init__(self, dictionary:tuple):
        assert len(dictionary) > 0
        self.__dictionary = dictionary
        self.__trieTree = TrieNode()
        self.__genTree()

    def __genTree(self):
        for word in self.__dictionary:
            self.__trieTree.insert(word)
            
    @staticmethod
    def __maxMatch(string, string1):
        array = [[0 for _ in range(len(string1))] for _ in range(len(string))]
        maxLength = 0
        for i in range(0, len(string)):
            for j in range(len(string1)):
                if string[i] == string1[j]:
                    array[i][j] = 1
                    if array[i-1][j-1] >= 1 and i > 0 and j > 0:
                        array[i][j] = array[i-1][j-1] + 1
            if max(array[i]) > maxLength:
                maxLength = max(array[i])
        return abs(len(string) - maxLength)
            

    def search(self, word, maxCost=0, showInfo=False):
        if maxCost == 0:
            maxCost = len(word)
        currentRow = list(range(len(word) + 1))
        results = []    
        for letter in self.__trieTree.children:
            self.__searchRecursive(self.__trieTree.children[letter], letter, word, currentRow, results, maxCost)
        if showInfo:
            print(f'***Search [{word}]***')
            for word in results:
                print(f'- {word}')
            print('***')
        if results:
            return min(results)[-1]
        return ''

    def __searchRecursive(self, node, letter, word, previousRow, results, maxCost):
        columns = len(word ) + 1
        currentRow = [previousRow[0] + 1]
        for column in range(1, columns):
            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                replaceCost = previousRow[ column - 1 ] + 1
            else:                
                replaceCost = previousRow[ column - 1 ]

            currentRow.append(min(insertCost, deleteCost, replaceCost))
            
        if currentRow[-1] <= maxCost and node.word != None:
            results.append((currentRow[-1] + self.__maxMatch(word, node.word), node.word))
            
        if min(currentRow) <= maxCost:
            for letter in node.children:
                self.__searchRecursive(node.children[letter], letter, word, currentRow, results, maxCost)


def main():
    dictPath = 'dict.txt' # Replace it with path to dictionary.txt
    assert os.path.exists(dictPath)
    with open(dictPath) as f:
        data = f.read().strip().split('\n')
    autoCorrect = AutoCorrect(tuple(data))
    while True:
        getInput = input('Type something: ').strip().split()
        for idx, word in enumerate(getInput):
            getInput[idx] = autoCorrect.search(word, showInfo=True)
        getInput = ' '.join(getInput)
        print(f'{"=" * len(getInput)}\n{getInput}\n{"=" * len(getInput)}')
        
