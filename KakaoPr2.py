
def solution(queue1, queue2):
    queue3 = queue1+queue2
    resultnum = int(sum(queue3))/2
    target = []
    answer = 0
    anlen = [1000000000]
    for i in range(len(queue3)+1):
        for j in range(len(queue3)+1):
            if(sum(queue3[i:j])==resultnum):
                target.append(queue3[i:j])
                num = (i)+(j-len(queue1))
                if num<0:
                    num = 10000000000
                anlen.append(num)
    answer = min(anlen)
    if(sum(queue3)%2 ==1):
        answer = -1
    if(len(target)==0):
        answer = -1

    return answer


print('q1 = ',solution([10,2,1,2],[1,1,1,2]))#queue 합이 15가 되어야함.(
print('q2 = ',solution([3,2,7,2],[4,6,5,1]))
