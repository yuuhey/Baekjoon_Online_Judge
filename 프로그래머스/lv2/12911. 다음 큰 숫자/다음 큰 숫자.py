def solution(n):
    n2 = bin(n)[2:]
    answer = n+1
    while str(n2).count("1") != str(bin(answer))[2:].count("1"):
        answer += 1
    return answer