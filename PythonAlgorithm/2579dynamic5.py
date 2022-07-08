N = int(input())
f_list = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(N):
    f_list[i] = int(input())
dp[0] = f_list[0]
dp[1] = f_list[0]+f_list[1]
dp[2] = max(f_list[1]+f_list[2],f_list[0]+f_list[2])
for i in range(3,N):
    dp[i] = max(dp[i-3]+f_list[i]+f_list[i-1],dp[i-2]+f_list[i])

