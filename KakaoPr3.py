def solution(survey, choices):

    answer = ''
    score = {"R":0, "T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}


    for first in range(len(survey)):
        target = list(survey[first])
        if choices[first] == 1:
            score[target[0]]+=3
        if choices[first] == 2:
            score[target[0]] += 2
        if choices[first] == 3:
            score[target[0]] += 1
        if choices[first] ==5:
            score[target[1]] += 1
        if choices[first] == 6:
            score[target[1]] += 2
        if choices[first] == 7:
            score[target[1]] += 3

    if score["R"]<score["T"]:
        answer +="T"
    else:
        answer += "R"


    if score["C"]>=score["F"]:
        answer +="C"
    else:
        answer += "F"
    if score["J"]>=score["M"]:
        answer +="J"
    else:
        answer += "M"
    if score["A"]>=score["N"]:
        answer +="A"

    else:
        answer += "N"


    return answer



print(solution(["AN","CF","MJ","RT","NA"],[5,3,2,7,5]))