def solution(board, moves):
    stack = []
    answer = 0
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                stack.append(board[i][move-1])
                board[i][move-1] =0
                if len(stack)>=2 and stack[-1] == stack[-2]:
                    stack = stack[:-2]
                    answer +=2
                break
            continue
    
    return answer