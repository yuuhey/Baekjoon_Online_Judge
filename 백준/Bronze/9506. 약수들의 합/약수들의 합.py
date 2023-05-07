from sys import stdin
input = stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    else:
        lst = []
        for i in range(1,n//2+1):
            if n%i==0:
                lst.append(i)
        if sum(lst) == n:
            print(n, '=', end=' ')
            print(*lst, sep=' + ')
        else:
            print(n, 'is NOT perfect.')