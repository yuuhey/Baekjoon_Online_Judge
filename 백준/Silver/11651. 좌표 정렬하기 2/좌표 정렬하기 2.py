lst = []
for i in range(int(input())):
    lst.append([*map(int, input().split())])
lst.sort(key=lambda x:(x[1],x[0]))
for i in lst:
    print(*i)