import sys
N = sys.stdin.readline()
P = list(map(int, sys.stdin.readline().split(' ')))

P.sort()
result =0
for i in range(len(P)):
    for j in range(i+1):
        result += P[j]


print(result)