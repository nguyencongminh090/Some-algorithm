'''
    For analysis data
    ** 14/4/2021 - 10:35 PM
'''

##data = [[1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7], [6, 10]]
##data = [[0, 0], [0, 2], [1, 1], [1, 3], [1, 4], [2, 0], [2, 2], [2, 4], [3, 1], [3, 3], [4, 0], [4, 2], [5, 1], [5, 3], [6, 0], [6, 2], [7, 1], [7, 3], [8, 0], [8, 2], [9, 1], [9, 3], [10, 0], [10, 2], [11, 1], [11, 3], [12, 0], [12, 2], [13, 1], [13, 3], [14, 0], [14, 2]]
data = [[0, 1], [0, 3], [0, 6], [1, 0], [1, 2], [1, 4], [1, 5], [1, 7], [1, 8], [1, 9], [2, 2], [2, 3], [2, 6], [2, 7], [2, 9], [3, 0], [3, 1], [3, 4], [3, 5], [3, 8], [4, 1], [4, 2], [4, 3], [4, 4], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 5], [6, 2], [6, 3], [6, 7], [6, 9], [6, 10], [7, 0], [7, 1], [7, 3], [7, 4], [7, 5], [7, 6], [7, 9], [8, 2], [8, 7], [8, 8], [9, 1], [9, 4], [9, 5], [9, 6], [9, 9], [9, 10], [10, 0], [10, 3], [10, 4], [10, 8], [11, 0], [11, 1], [11, 2], [11, 5], [11, 6], [11, 7], [11, 8], [11, 10], [12, 3], [12, 5], [12, 8], [13, 0], [13, 1], [13, 2], [13, 4], [13, 8], [13, 9], [13, 10], [14, 1], [14, 3], [14, 5], [14, 6], [14, 9], [14, 10]]
def lgs(data):
    for i in range(len(data)):        
        stack = []
        if data[i][0] < max(data)[0]:
            for j in range(len(data)):
                if data[j][0] == data[i][0] + 1:
                    stack.append(data[j])
        c = 0
        lta = []
        for j in range(len(data)):
            if data[i][0] == data[j][0]:
                c += 1
                lta.append(data[j])
        if c >= 5:
            lta.sort()
            stack = lta                
        print('Start with', data[i])
        print('---> Stack:', stack)
        while stack:
            lst = [data[i]]
            rx = stack[0][0] - data[i][0]
            ry = stack[0][1] - data[i][1]
            if abs(rx) > 1 or abs(ry) > 1 or (rx, ry) == (0, 0):
                stack.remove(stack[0])
                continue
            
            print('\tCurrent LST:', lst)
            print('\tCurrent Stack:', stack[0])
            print('\tRule: {}, {}'.format(rx, ry))

            x = lst[0][0] + rx
            y = lst[0][1] + ry
            while [x, y] in data:
                lst.append([x, y])
                x += rx
                y += ry

            if len(lst) == 5:
                x = lst[0][0] - rx
                y = lst[0][1] - ry
                while [x, y] in data:
                    lst.insert(0, [x, y])
                    x -= rx
                    y -= ry
                    if c > 5:
                        break
            
            
            print('\t---> LST:', lst)
            if len(lst) == 5:
                break
            elif len(lst) > 5:
                print('LEN: {}, PV: {}'.format(len(lst), lst))
            stack.remove(stack[0])            
        print('\tAvailable Stack:', stack)
        if len(lst) == 5:
            break
    try:
        if len(lst) == 5:
            print('FOUND WIN:', lst)
            return True
        else:
            return False
    except:
        return False

print('Data:', data)
data.sort()
lgs(data)
        
