def solution(s):
    stack = []
    answer = True
    for i in list(s):
        if i == "(":
            stack.append("(")
        elif i == ")":
            try:
                stack.pop()
            except:
                answer = False
    if len(stack) != 0:
        answer = False
    return answer