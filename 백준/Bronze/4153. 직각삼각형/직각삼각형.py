while True:
    lst = [*map(int, input().split())]
    if lst == [0,0,0]:
        break
    lst = sorted(lst)
    if lst[2]**2 ==lst[0]**2+lst[1]**2:
        print("right")
    else:
        print("wrong")