### Author Nguyen Cong Minh

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
    
def lgs(data):
    # LOGIC_SEARCH ALGORITHM | BY NGUYEN CONG MINH 16/4/2021 - 10:07 PM
    a = clock()
    for i in range(len(data)):
        stack = []
        if data[i][0] < max(data)[0]:
            for j in range(len(data)):
                if data[j][0] == data[i][0] + 1:
                    stack.append(data[j])
        c = 0
        lta = []
        lst = []
        for j in range(len(data)):
            if data[i][0] == data[j][0]:
                c += 1
                lta.append(data[j])
        if c >= 5:
            lta.sort()
            stack = lta
        while stack:
            lst = [data[i]]
            rx = stack[0][0] - data[i][0]
            ry = stack[0][1] - data[i][1]
            if abs(rx) > 1 or abs(ry) > 1 or (rx, ry) == (0, 0):
                stack.remove(stack[0])
                continue
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
            if len(lst) == 5:
                break
            stack.remove(stack[0])
        if len(lst) == 5:
            break
    try:
        if len(lst) == 5:
            b = clock()
            print('FOUND WIN:', lst)
            
            print('Runtime: %.7f sec' % (b - a))
            return True
        else:
            b = clock()
            print('Runtime: %.7f sec' % (b - a))
            return False
    except:
        b = clock()
        print('Runtime: %.7f sec' % (b - a))
        return False
        

def is_win(data):
    db = []
    dw = []
    for i in range(len(data)):
        if i % 2 == 0:
            db.append(data[i])
        else:
            dw.append(data[i])
    db.sort()
    dw.sort()
    print('List of Black:', db)
    print('List of White:', dw)
    result_b = lgs(db)
    print('--> Black Win:', result_b)

    result_w = lgs(dw)
    print('--> White Win:', result_w)
    print()
    return 'Done!!!'


while True:
    fin = input('File name: ')
    data = ofn(fin)
    if data == -1:
        print('\t(File can not load --> Corrupt/ Not available!')
        continue
    print('DATA:', data)
    print()
    print('Output:', is_win(data))
    inp = input('Quit? y/n: ')
    if inp.upper() == 'Y':
        break
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
