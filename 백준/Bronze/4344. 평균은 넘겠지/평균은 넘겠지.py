N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:])/lst[0]
    count = 0
    for i in lst[1:]:
        if i>avg:
            count += 1
    # print(str('{:.3f}'.format(round(count/lst[0]*100, 3)))+"%")
    per = (count/lst[0])*100
    print('%.3f' % per + '%')