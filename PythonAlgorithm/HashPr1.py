# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i,j in zip(participant,completion):
#         if i!=j:
#             print(i)
#             return i
#
#     return participant.pop()

import collections
def solution(participant, completion):
    test_hash = collections.Counter(participant)-collections.Counter(completion)
    print(test_hash)
    return list(test_hash.keys())[0]
a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]
print(solution(a,b))