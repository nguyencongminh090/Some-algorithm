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
                return True
    return False
        

def is_win(data):
    db = data[::2]
    dw = data[1::2]
    a = clock()
    lgs(db)
    b = clock()
    print('Len:', len(db))
    print('Runtime: %.7f sec' % (b - a))    
    print()
    a = clock()
    lgs(dw)
    b = clock()
    print('Len:', len(dw))
    print('Runtime: %.7f sec' % (b - a))
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
    
