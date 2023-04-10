n, m = map(int, input().split())
A, B= [],[]
C = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    A.append([*map(int, input().split())])
for _ in range(n):
    B.append([*map(int, input().split())])

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j]+B[i][j]
        
for i in C:
    for j in i:
        print(j,end=" ")
    print()