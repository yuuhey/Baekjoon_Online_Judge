from sys import stdin
import bisect
input = stdin.readline

input()
lst1 = [*map(int, input().split())]
input()
lst2 = [*map(int, input().split())]
lst1.sort()

for i in lst2:
    if lst1[bisect.bisect(lst1,i)-1]==i:
        print(1, end=' ')
    else:
        print(0, end = ' ')