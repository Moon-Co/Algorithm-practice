def solution(s):
    number = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    new = []
    newnew = []
    for i in s:
        new.append(i)
        result = ''.join(s for s in new)
        if result in number:
            newnew.append(number.index(result))
            result = ""
            new=[]
        if result.isdigit() == True:
            newnew.append(int(result))
            result = ""
            new = []
    answer = ''.join(map(str,newnew))
    answer = int(answer)



    return answer


print(solution("one4seveneight"))