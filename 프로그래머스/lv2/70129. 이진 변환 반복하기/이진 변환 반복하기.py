def solution(s):
    n, zero = 0, 0
    while s!="1":
        n+=1
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
    return [n, zero]