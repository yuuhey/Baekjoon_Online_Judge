d = {}
for _ in range(int(input())):
    n, s = map(str, input().split())
    d[n] = s
answer = []
for key, value in d.items():
    if value == 'enter':
        answer.append(key)
answer.sort(reverse=True)
for i in answer:
    print(i)