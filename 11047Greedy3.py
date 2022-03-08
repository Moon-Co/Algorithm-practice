# import sys
#
# N,K = list(map(int,sys.stdin.readline().split()))
# won = []
# count = 0
# for i in range(N):
#     money = int(input())
#     won.append(money)
# while K!=0:
#     new_list = []
#     for i in won:
#         if i <=K:
#             new_list.append(i)
#     K = K-max(new_list)
#     count+=1
#
# print(count)
# -> Timeout

n,k = map(int,input().split())

m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in reversed(range(n)):
    if k==0:
        break
    if m[i]>k:
        continue
    num+=k//m[i] #
    k%=m[i]
print(num)
