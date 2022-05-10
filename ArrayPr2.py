
def solution(numbers):
    result = []
    a = []
    for i in range(len(numbers)):
        if numbers[i] <10:
            result.append([numbers[i]*1000,numbers[i]])
        elif numbers[i] <100:
            result.append([numbers[i]*100,numbers[i]])
        elif numbers[i] <1000:
            result.append([numbers[i]*10,numbers[i]])
        else:
            result.append([numbers[i],numbers[i]])
    result.sort(key=lambda x: x[1], reverse=False)
    result.sort(key=lambda x: x[0],reverse = True)


    for j in range(len(result)):
        a.append(result[j][1])
    rs = ''.join(map(str,a))

    return rs


print(solution([10,9,19,19]))