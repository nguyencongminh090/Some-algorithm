
'''
    if x <= 11 and 5<=y<=11
    wincase1    x = x , y giam
    wincase2    x tang , y giam
    wincase3    x tang , y =y
    wincase4    x tang , y tang
    wincase5    x = x , y tang
'''
from time import perf_counter as clock

def ofn(fin):
    try:
        f = open(fin)
        f = f.readlines()
        f = [i.split('\n')[0] for i in f][1:-1]
        for i in range(len(f)):
            f[i] = [int(f[i].split(',')[0]) - 1, int(f[i].split(',')[1]) - 1]
        return f
    except:
        return -1

def find_win(move,player_moves):
    x,y = move[0],move[1]
    lines = [([[x,y+i] for i in range(5)],[x,y-1],[x,y+5]),
            ([[x+i,y+i] for i in range(5)],[x-1,y-1],[x+5,y+5]),
            ([[x+i,y] for i in range(5)],[x-1,y],[x+5,y]),
            ([[x+i,y-i] for i in range(5)],[x-1,y+1],[x+5,y-5]),
            ([[x,y-i] for i in range(5)],[x,y+1],[x,y-5])]
    for line,first,last in lines:
        lst = []
        for i in range(len(line)):
            if line[i] in player_moves:
                lst.append(line[i])
            else:
                break 
        if len(lst)==5:
            if first in player_moves or last in player_moves:
                continue
            return lst
        
def is_win(player_moves):
    a = clock()
    move_pos = 0
    while move_pos< len(player_moves):
        WIN = find_win(player_moves[move_pos],player_moves)
        if WIN != None:
            b = clock()
            return WIN, round(b-a, 7)
        move_pos+= 1
    b = clock()
    return 'No win', round(b-a, 7)

while True:
    inp = input('File name: ')
    moves = ofn(inp + '.psq')
    try:        
        black = moves[::2]
        white = moves[1::2]
        
        print(is_win(black))
        print(is_win(white))
    except:
        black = moves[::2]
        print(black)
        pass
