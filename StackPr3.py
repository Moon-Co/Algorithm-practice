def solution(prices):
    answer = []
    for i in range(len(prices)):
        target = 0
        for j in range(i+1, len(prices)):
            target +=1
            if prices[j]>=prices[i]:
                continue
            else:
                break
        answer.append(target)
    answer[-1] = 0
    return answer

print(solution([1,2,3,2,3]))