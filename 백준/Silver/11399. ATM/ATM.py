input()
lst = list(map(int, input().split()))
lst.sort()
dp = [0]*len(lst)
dp[0] = lst[0]
for i in range(1, len(lst)):
    dp[i] = dp[i-1]+lst[i]
print(sum(dp))