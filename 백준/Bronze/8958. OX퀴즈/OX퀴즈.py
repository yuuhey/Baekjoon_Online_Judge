
for _ in range(int(input())):
    s = str(input())
    ans, count = 0, 0
    for i in s:
        if i == "O":
            count +=1
            ans +=count
        if i == "X":
            count = 0
    print(ans)