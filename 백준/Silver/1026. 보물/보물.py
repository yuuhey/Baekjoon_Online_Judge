def S(li1, li2):
    li1.sort()
    li2.sort(reverse=True)
    sum = 0
    for i in range(len(li1)):
        sum += li1[i]*li2[i]
    print(sum)
input()
S(list(map(int, input().split())), list(map(int,input().split())))