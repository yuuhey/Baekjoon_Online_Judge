def solution(t, p):
    count = 0
    p_len = len(p)
    for i in range(len(t)-p_len+1):
        if int(p)>=int(t[i:i+p_len]):
            count +=1
    return count