def solution(operations):
    answer = []

    for i in operations:
        current, num = i.split()
        if current == "I":
            answer.append(int(num))
        else:
            if num == "-1":
                # print(min(answer))
                answer.pop(answer.index(min(answer)))
                print(answer,'a')

            else:
                print(answer,'b')
                answer.pop(answer.index(max(answer)))
    if len(answer) == 0:
        answer = [0, 0]
    a = max(answer)
    b = min(answer)
    answer = [a,b]
    return answer


# solution(["I 7","I 5","I -5","D -1"])
print(solution(["I 16", "D 1"]))