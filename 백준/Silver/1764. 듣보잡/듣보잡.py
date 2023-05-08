from collections import Counter

n, m = map(int,input().split())
li = []
for i in range(n+m):
    li.append(str(input()))

counter = Counter(li)
c = 0
lst = []
for key, value in counter.items():
    if value>1:
        lst.append(key)
        c += 1
print(c)
lst.sort()
for i in lst:
    print(i)