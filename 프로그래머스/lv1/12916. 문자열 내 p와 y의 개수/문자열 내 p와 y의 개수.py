def solution(s):
    answer = True
    if s.upper().count('P') != s.upper().count('Y'):
        return False
    return True