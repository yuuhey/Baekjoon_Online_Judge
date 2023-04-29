lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:x[1])
lst.sort()
for i in lst:
    print(*i)