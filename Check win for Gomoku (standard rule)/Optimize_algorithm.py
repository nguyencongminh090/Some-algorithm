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
        rule = [[1, 0], [0, 1], [1, -1], [1, 1]]
        for rx, ry in rule:
            lst = [data[i]]
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
            if len(lst) == 5:
                break
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
    result_b = lgs(db)
    print('--> Black Win:', result_b)
    print()
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
    print()
    print('Output:', is_win(data))
    inp = input('Quit? y/n: ')
    if inp.upper() == 'Y':
        break
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
