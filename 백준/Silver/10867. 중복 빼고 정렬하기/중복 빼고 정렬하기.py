input()
li = list(set(list(map(int, input().split()))))
li.sort()
print(*li)