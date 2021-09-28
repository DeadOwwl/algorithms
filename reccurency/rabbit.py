def rabbit_jumping(n, w):
    if n == 0 or n == 1:
        w.write('1')
    elif n == 2:
        w.write('2')
    else:
        first = 1
        second = 2
        third = 0
        i = 2
        while i != n:
            third = (first + second) % 1000000007
            first = second % 1000000007
            second = third % 1000000007
            i = i + 1
        w.write(str(third))


f = open('input.txt')
m = int(f.readline())
w = open('output.txt', 'w')
rabbit_jumping(m, w)