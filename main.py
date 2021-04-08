import sys


def delete_Zero(m):
    k = 0
    a = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                k += 1
        if k != len(m[i]):
            a.append(i)
        k = 0
    return a


def delete_Zero1(m):
    k = 0
    a = []
    for i in range(len(m[1])):
        for j in range(len(m)):
            if m[j][i] == 0:
                k += 1
        if k != len(m):
            a.append(i)
        k = 0
    return a


def print_M(m):
    a = delete_Zero(m)
    b = delete_Zero1(m)
    m2 = []
    for i in a:
        m1 = []
        for j in b:
            m1.append(m[i][j])
        m2.append(m1)
    return m2


def exit_f():
    f_end = open(sys.argv[2], "w+")
    i = 0
    while i < len(rez):
        j = 0
        while j < len(rez[i]):
            s = str(rez[i][j])
            f_end.write(s + ' ')
            j = j + 1
        f_end.write('\n')
        i = i + 1
    f_end.close()


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        f = file.readlines()
        matrix = [[int(n) for n in x.split()] for x in f]

    rez = print_M(matrix)

    exit_f()