N = int(input())
first_list = list(map(int,input().split()))
second_list = list(map(int,input().split()))
first_list.sort()
second_list.sort()
y = reversed(second_list)
y = list(y)
sum = 0
for i in range(N):
    sum += first_list[i]*y[i]
print(sum)