N = int(input())

def onetwothree(num):

    if num ==1:
        return 1
    elif num ==2:
        return 2
    elif num==3:
        return 4

    return onetwothree(num-1)+onetwothree(num-2)+onetwothree(num-3)

for i in range(N):
     target = int(input())
     print(onetwothree(target))