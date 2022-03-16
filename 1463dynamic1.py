n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):#have to do all case
    dp[i] = dp[i - 1] + 1#-1이 제일 작으면 이전거에 1 더한거

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[n]) #failed