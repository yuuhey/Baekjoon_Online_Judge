from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
n_lst = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
m_lst = list(map(int, stdin.readline().split()))

count = Counter(n_lst)

for i in m_lst:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')