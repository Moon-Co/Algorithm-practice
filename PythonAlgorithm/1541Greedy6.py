# cal = str(input())
# cal = list(cal)
# new_list = []
# count =0
# for i in cal:
#     if i =='-'and count>0:
#         i= ')-('
#     if i =='-':
#         i = '-('
#         count+=1
#     new_list.append(i)
# for j in range(count):
#     new_list.append(')')
#
# cal= ''.join(new_list)
# cal = eval(cal)
# print(cal)
#-> runtime Error
N = input().split('-')
num = []
for i in N:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)
n = num[0]
for i in range(1,len(num)):
    n-=num[i]
print(n)




