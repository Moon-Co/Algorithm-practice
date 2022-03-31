import numpy as np

def solution(progresses, speeds):
    progresses = np.array(progresses)
    speeds = np.array(speeds)
    answer = []
    for i in range(100):
        progresses = progresses+speeds
        k=0
        if progresses[0] >=100:
            while progresses[0]>=100:
                progresses = np.delete(progresses,0)
                speeds = np.delete(speeds,0)
                k+=1
                if len(progresses)==0:
                    answer.append(k)
                    return answer
            answer.append(k)

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
