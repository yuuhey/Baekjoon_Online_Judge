from collections import Counter

def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    answer = []
    for i in photo:
        sum = 0
        dic = dict(Counter(i))
        for i in dic:
            try:
                sum += dictionary[i]*dic[i]
            except:
                continue
        answer.append(sum)
    return answer