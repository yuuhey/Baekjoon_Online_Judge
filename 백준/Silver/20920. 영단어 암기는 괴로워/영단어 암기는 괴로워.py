import collections

N, M = map(int, input().split())
d = []
for _ in range(N):
    i = input()
    if len(i) >= M:
        d.append(i)
dic = collections.Counter(d)
dic = sorted(dic.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))

for word in dic:
    print(word[0])