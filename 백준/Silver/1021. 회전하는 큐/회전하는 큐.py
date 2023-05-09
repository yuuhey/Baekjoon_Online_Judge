from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
loc = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

c = 0
for l in loc:
    while True:
        if dq[0] == l:
            dq.popleft()
            break
        else:
            if dq.index(l) < len(dq)/2: # 뽑으려는 수의 위치 인덱스가 큐의 길이/2보다 작을 때는 왼쪽으로 움직여야 최소
                while dq[0] != l:
                    dq.append(dq.popleft())
                    c += 1
            else: # 뽑으려는 수의 위치 인덱스가 큐의 길이/2보다 클 때는 오른쪽으로 움직여야 최소
                while dq[0] != l:
                    dq.appendleft(dq.pop())
                    c += 1
print(c)