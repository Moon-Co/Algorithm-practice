import sys
N = int(sys.stdin.readline())
rope_list=[]
weight_list =[]
for _ in range(N):
    rope = int(sys.stdin.readline())
    rope_list.append(rope)
##배열의 최소값 *길이 하고 최소값 배열에서 없애고 반복
sorted_list = sorted(rope_list)
for i in range(N):
    weight_list.append(len(sorted_list)*sorted_list[0])
    del sorted_list[0]
print(max(weight_list))
