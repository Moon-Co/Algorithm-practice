def solution(rc, operations):

    for i in operations:
        if i == "ShiftRow":
            tmp = rc[0]
            for j in range(1,len(rc)):
                rc[j-1] = rc[j]
            rc[-1] = tmp
        if i == "Rotate":
            rightdown = rc[-1][-1]
            lefttop = rc[0][0]
            for c in range(len(rc)-1,0,-1):
                rc[c][-1] = rc[c-1][-1]
                rc[-c-1][0] = rc[-c][0]
            for j in range(2,len(rc[0])):

                rc[0][-j+1] = rc[0][-j]
                rc[-1][j-2] = rc[-1][j-1]
            rc[0][1] = lefttop
            rc[-1][-2] = rightdown




    return rc

print(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12]],
               ["Rotate"]))