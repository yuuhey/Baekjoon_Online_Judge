def solution(today, terms, privacies):
    contract ={}
    today_lst = list(map(int,today.split('.')))
    answer = []
   
    for term in terms:
        s, l = term.split()
        contract[s] = int(l)*28
    for i in range(len(privacies)):
        date, s = privacies[i].split()
        date_lst = list(map(int, date.split('.')))
        year = (today_lst[0] - date_lst[0])*336
        month = (today_lst[1]-date_lst[1])*28
        day = today_lst[2] - date_lst[2]
        total = year+month+day
        if contract[s] <= total:
            answer.append(i+1)
    return answer