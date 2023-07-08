from collections import deque

queue = deque()
r = 0
for _ in range(int(input())):
    n = input()
    if n == 'ENTER':
        r += len(set(queue))
        queue = deque()
    else:
        queue.append(n)
r += len(set(queue))
print(r)