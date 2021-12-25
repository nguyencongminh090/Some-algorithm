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
            if [lst[0][0] + rx * 4, lst[0][1] + ry * 4] not in data or \
               [lst[0][0] + rx * 3, lst[0][1] + ry * 3] not in data or \
               [lst[0][0] + rx * 2, lst[0][1] + ry * 2] not in data or \
               [lst[0][0] + rx * 1, lst[0][1] + ry * 1] not in data \
               or [lst[0][0] + rx * 5, lst[0][1] + ry * 5] in data or [lst[0][0] - rx, lst[0][1] - ry] in data:
                continue
            else:
                b = clock()
                print('Runtime: %.7f sec' % (b - a))
                lst = [[lst[0][0] + rx * k, lst[0][1] + ry * k] for k in range(5)]
                print('FOUND WIN:', lst)
                return True
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
    
