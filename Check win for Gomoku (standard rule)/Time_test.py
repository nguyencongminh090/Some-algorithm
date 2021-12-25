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


def test_time(func, n, path='testcase\\'):
    time_black = 0
    min_black = 10**4
    max_black = 10**4*-1
    case_min_black = ''
    case_max_black = ''
    
    time_white = 0
    min_white = 10**4
    max_white = 10**4*-1
    case_min_white = ''
    case_max_white = ''
    for i in range(n):
        f = ofn(f'{path}{i+1}.psq')
        black = f[::2]
        white = f[1::2]
        
        t1 = clock()
        result_b = func(black)
        t2 = clock()
        cvt_time = '{:.7f}'.format(t2-t1)
        print(f'[+] Case {i+1} (black) | Len: {len(black)} | Runtime: {cvt_time} sec | OUTPUT: {result_b}' )
        if t2 - t1 < min_black:
            min_black = t2 - t1
            case_min_black = f'Case_min_black {i+1}.psq'
        if t2 - t1 > max_black:
            max_black = t2 - t1
            case_max_black = f'Case_max_black {i+1}.psq'
        time_black += t2 - t1
        
        t1 = clock()
        result_w = func(white)
        t2 = clock()
        cvt_time = '{:.7f}'.format(t2-t1)
        print(f'[+] Case {i+1}  (white)| Len: {len(white)} | Runtime: {cvt_time} sec | OUTPUT: {result_w}')
        time_white += t2 - t1
        if t2 - t1 < min_white:
            min_white = t2 - t1
            case_min_white = f'Case_min_white {i+1}.psq'
        if t2 - t1 > max_white:
            max_white = t2 - t1
            case_max_white = f'Case_max_white {i+1}.psq'

    print('-'*10)
    print('***REPORT***')
    print(f'- Black:\n+ Min time: {min_black}\n+ Testcase: {case_min_black}\n+ Max time: {max_black}\n+ Testcase: {case_max_black}\n==> Total time: {time_black}')
    print(f'- White:\n+ Min time: {min_white}\n+ Testcase: {case_min_white}\n+ Max time: {max_white}\n+ Testcase: {case_max_white}\n==> Total time: {time_white}')
    return
        
    
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


test_time(lgs, 33)
