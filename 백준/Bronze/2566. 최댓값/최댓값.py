A = []
row, col = 0, 0
MAX = -1
for _ in range(9):
    A.append([*map(int, input().split())])
for i in range(9):
    for j in range(9):
        if A[i][j] > MAX:
            MAX = A[i][j]
            row = i+1
            col = j+1
print(MAX)
print(row,col)