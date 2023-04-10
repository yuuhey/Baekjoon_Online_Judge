def solution(brown, yellow):
    total = brown + yellow
    for i in range(yellow, 0, -1):
        if yellow%i==0:
            if (i+(yellow//i))*2+4 == brown:
                answer = [yellow//i+2,i+2]
    return answer