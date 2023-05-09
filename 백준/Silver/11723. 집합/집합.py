import sys

input = sys.stdin.readline
n = int(input())

s = set()

for i in range(n):
    command = list(input().split())

    if len(command) == 1:
        if command[0] == 'all':
            s = set([i for i in range(1, 21)])
        else: # command[0] == 'empty':
            s = set()
        continue

    cmd = command[0]
    target = int(command[1])

    if cmd == 'add':
        s.add(target)
    elif cmd == 'remove':
        s.discard(target)
    elif cmd == 'check':
        if target in s:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)