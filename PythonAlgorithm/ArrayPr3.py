def solution(citations):
    answer = 0
    a= len(citations)
    count = 0
    breaker = 0
    for i in range(len(citations),0,-1):
        for j in range(len(citations)):
            if citations[j]>=i:
                count+=1
            if count== i:
                answer = count
                breaker = 1
                break
        if breaker ==1:
            break
        count = 0


    return answer



print(solution([3,0,6,1,5])) #2여야해 답이. [2,3,7,8,11]이라면?  #3이어야해
#[1,7,8,9]라면? : 3이어야해 (length가 최댓값인데, 4-> 4보다 큰거 3개뿐 3-> 3보다 큰거 3개! 2->2보다큰거 3개