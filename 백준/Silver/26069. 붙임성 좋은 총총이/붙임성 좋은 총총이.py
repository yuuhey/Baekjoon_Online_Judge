s = {"ChongChong"}
for _ in range(int(input())):
    n, m = input().split()
    if n in s or m in s:
        s.update([n, m])
print(len(s))