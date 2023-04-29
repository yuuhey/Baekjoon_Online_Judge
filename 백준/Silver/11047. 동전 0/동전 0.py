n, k = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst = list(reversed(sorted(lst)))

c = 0
while k!=0:
    for i in lst:
        if k//i>0:
            c += k//i
            k = k%i
print(c)