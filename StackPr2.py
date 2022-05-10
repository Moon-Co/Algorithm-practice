def solution(priorities, location):
    stack = list()
    pri = list()
    array2 = list()
    for i in priorities:
        stack.append(i)
    array1 = [c for c in range(len(priorities))]  # index 위치 저장
    i = 0
    while i < len(priorities):
        a = stack.pop(0)
        b = array1.pop(0)

        # print(min(array1))
        if a < max(stack):
            stack.append(a)
            array1.append(b)
        else:
            pri.append(a)
            array2.append(b)
        i += 1
    # print(array2)
    for i in range(0, len(stack), 1):
        c = stack.pop(0)
        d = array1.pop(0)
        pri.append(c)
        array2.append(d)
    # print(pri)
    # print(array2)
    print(array2.index(location) + 1)
# solution([2,1,3,2],2) #result 1