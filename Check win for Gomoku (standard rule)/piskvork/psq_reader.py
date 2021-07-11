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


def write_psq(data):
    f = open('23.psq', 'w')
    f.write('Piskvorky 15x15, 0:0, 0\n')
    for i in range(len(data)):
        f.write(str(data[i][0]+2) + ', ' + str(data[i][1] + 2) + '\n')
    f.write('-1')
    f.close
    pass


##data = ofn('22.psq')

write_psq(data)
print(ofn('23.psq'))
