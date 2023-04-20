for _ in range(int(input())):
    lst = list(input().split())
    if all(i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:" for i in lst[1]):
        for i in lst[1]:
            print(i*int(lst[0]), end="")
        print()