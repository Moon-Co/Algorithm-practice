# import sys
#
# N = int(sys.stdin.readline())
# time_list=[]
# best_list = [[0,0]]
# minimum = 1e9
# for i in range(N):
#     start, end = list(map(int,sys.stdin.readline().split()))
#     time_list.append([start,end])
#
# for i in range(N):
#     minimum = 1e9
#     minidx = 0
#     for j in time_list:
#         #전꺼 끝나는시간-지금꺼 시작시간 + 지금꺼 끝나는시간-지금꺼 시작시간이 최소
#         #이전j[1]-현재[j[0]+현재j[1]-현재j[0]가 최소여야해-> best_list에 append
#         start_diff = j[0]-best_list[i][1]
#         end_diff = j[1]-j[0]
#         if start_diff>0 and start_diff+end_diff<minimum:
#             minimum = start_diff+end_diff
#             minidx = time_list.index(j)#타겟 항의 인덱스
#     best_list.append([time_list[minidx][0],time_list[minidx][1]])
# best_list =list(set([tuple(set(best_list))for best_list in best_list]))
# print(len(best_list)-1)
#
n = int(input())
s = []
for i in range(n):
    first, second = map(int,input().split())
    s.append([first,second])
s = sorted(s,key = lambda a:a[0])
s = sorted(s,key=lambda a:a[1])
last = 0
cnt = 0
for i,j in s:
    if i>=last:
        cnt+=1
        last = j

print(cnt)
