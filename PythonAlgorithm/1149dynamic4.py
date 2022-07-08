N = int(input())
h_list= []

result_list = []
for _ in range(N):
    R,G,B = list(map(int,input().split()))
    h_list.append([R,G,B])
#main idea = 두번째 항부터, 전에 남은것중에 작은거랑 자기를 더한값에 본인을 할당한다.
for i in range(1,len(h_list)):
    h_list[i][0] = min(h_list[i-1][1],h_list[i-1][2])+h_list[i][0]
    h_list[i][1] =min(h_list[i-1][0],h_list[i-1][2])+h_list[i][1]
    h_list[i][2] =min(h_list[i-1][0],h_list[i-1][1])+h_list[i][2]


print(min(h_list[N-1][0],h_list[N-1][1],h_list[N-1][2]))




