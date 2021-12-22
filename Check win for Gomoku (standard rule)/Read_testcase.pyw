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
    
while True:
    fin = input('File name: ')
    data = ofn(fin)
    
    if data == -1:
        print('\t(File can not load --> Corrupt/ Not available!')
        continue
    print(data)
    inp = input('Quit? y/n: ')
    if inp.upper() == 'Y':
        break
    else:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
