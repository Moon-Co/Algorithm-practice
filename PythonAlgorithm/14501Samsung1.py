N = int(input())
work_list = []
money_list = []
result_list = []
for _ in range(N):
    a,b = list(map(int,input().split()))
    work_list.append(a)
    money_list.append(b)
    result_list.append(b)
result_list.append(0)


for i in range(N-1,-1,-1):
    print(i)
    if work_list[i]+i >N:
        result_list[i] = result_list[i+1]
    else:
        result_list[i] = max(result_list[i+1],money_list[i]+result_list[i+work_list[i]])
print(result_list[0])





