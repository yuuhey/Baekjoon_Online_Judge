import collections
c = collections.Counter(input().upper())
lst = list(c.values())
max_value = max(lst)
if lst.count(max_value)==1: # 개수가 하나이면
    print(list(c.keys())[lst.index(max_value)])
else:
    print("?")