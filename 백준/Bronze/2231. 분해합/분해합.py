n = int(input())
ans = 0
for i in range(n):
    if i+sum(map(int, str(i))) == n:
        ans = i
        break
print(ans)