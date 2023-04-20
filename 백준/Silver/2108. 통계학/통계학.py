from collections import Counter
lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
print(int(round(sum(lst)/n, 0)))
lst.sort()
print(lst[n//2])
cnt = Counter(lst).most_common()
if len(cnt)>1 and cnt[0][1]==cnt[1][1]:
  print(cnt[1][0])
else :
  print(cnt[0][0])

print(abs(max(lst)-min(lst)))