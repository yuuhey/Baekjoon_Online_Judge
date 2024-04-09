from collections import deque

def bfs(i, j, h):
    q = deque()
    q.append((i, j))
    v[i][j]=1

    while q:
        x, y = q.popleft()
        # 방향, 범위
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = x+di, y+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>h:
                q.append((ni, nj))
                v[ni][nj]=1

N = int(input())
arr = []
max_h = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    max_h = max(max_h, max(lst))
    
result = 0
for h in range(max_h+1):
    v = [[0]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and v[i][j] ==0:
                bfs(i, j, h)
                count += 1
    result = max(result, count)

print(result)
