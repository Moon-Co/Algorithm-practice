
def solution(clothes):
    answer = 1
    hash ={}
    for i in clothes:
        hash[i[1]] = 0
    for i in clothes:
        if i[1] in hash:
            hash[i[1]]+=1
            #각각의 옷이 몇개씩 있는지 고려

    for j in hash.values():
        answer *= (j+1)
        #모든 옷은 입는다/안입는다 경우가 있음. 옷이 2개일때는 1개 입는다,아무것도 안입는다 밖에 없음(경우의수 3개)
        #3개일때도 1개 입거나 아무것도 안입거나. (경우의수 4개)
        #각각 옷 종류마다 나오는 경우의수를 곱함.

    return answer-1 #전부 다 안입을 수는 없어서 1뺌

print(solution([["yellowhat", "headgear"],
                ["bluesunglasses", "eyewear"],
                ["green_turban", "headgear"]]))