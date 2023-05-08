from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
lst1= []
for _ in range(n):
    lst1.append(input())
lst1 = set(lst1)
c=0
for _ in range(m):
    t = input()
    if t in lst1:
        c +=1
print(c)