from itertools import combinations
from itertools import permutations
def solution(phone_book):

    phone_book = sorted(phone_book)
    print(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print('p1=',p1)
        print('p2=',p2)

        if p2.startswith(p1):
            return False
    return True

print(solution(["119","1243251435999","1195524421"]))

#     answer = True
#     hash = {}
#     for i in phone_book:
#         hash[i] = 1
#     for i in phone_book:
#         temp = ''
#         for j in i:
#             print(j)
#             temp += j
#             if temp in hash and temp != i:
#                 return False