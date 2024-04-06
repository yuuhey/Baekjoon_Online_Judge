def solution(n, lost, reserve):
    # 여벌의 체육복을 가져온 학생이 체육복을 도난당한 경우 처리
    lost_set = set(lost)
    reserve_set = set(reserve)
    lost = list(lost_set - reserve_set)  # 여벌의 체육복을 가져온 학생 제외
    reserve = list(reserve_set - lost_set)  # 체육복을 도난당한 학생 제외

    # 체육복을 빌려줄 수 있는 학생 수 계산
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    
    # 체육수업을 들을 수 있는 학생 수 반환
    return n - len(lost)