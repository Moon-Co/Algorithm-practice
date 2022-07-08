import heapq

def solution(operations):
    answer = []
    test=  []
    for i in range(len(operations)):
        test.append(operations[i].split())

    for j in test:
        if j[0]=='I':
            heapq.heappush(answer,int(j[1]))
        if j[0]=='D'and len(answer)>=1:
            if j[1] =='-1':
                heapq.heappop(answer)
            if j[1] == '1':
                print('a')
                heapq._heappop_max(answer)
    heapq.heapify(answer)
    if len(answer)==0:
        answer = [0,0]
    a = heapq.heappop(answer)
    heapq._heapify_max(answer)
    b = heapq._heappop_max(answer)
    answer = [b,a]
    return answer


print(solution(["I -5","I -5","I 5"]))