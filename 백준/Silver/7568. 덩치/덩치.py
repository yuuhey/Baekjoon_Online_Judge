lst = []
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))

for p in lst:
    score = 1
    for pair in lst:
        if pair[0]>p[0] and pair[1]>p[1]:
            score +=1
    print(score, end=" ")