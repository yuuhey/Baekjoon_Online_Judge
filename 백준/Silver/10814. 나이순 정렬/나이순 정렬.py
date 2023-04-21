lst = []
for _ in range(int(input())):
    lst.append([*input().split()])
lst.sort(key=lambda x:int(x[0]))
for i in lst:
    print(*i)