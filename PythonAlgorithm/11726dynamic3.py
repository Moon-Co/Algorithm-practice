
#1 = s =1
#2 = ss,gg=2
#3 = sss,sgg,ggs=3
#4 = ssss,ggss,sggs,ssgg,gggg=5
#5 = sssss,ggsss,sggss,ssggs,sssgg,sgggg,ggggs,qqsqq = 8
#0g = 1, 2g = 4(3s1g), 4g(1s1g) = 3
#6 = ssssss,qqssss,sqqsss,ssqqss,sssqqs,sqqqqs,qqqqss,qqsqqs,ssssqq,qqssqq,sqqsqq
#7 = 1 2g = 5s1g,  4g = 3s2g = ,  6g = 1s3g = 4
#9 = (0g = 1) (2g = 7s1g=7), (4g = 5s2g = ), (6g= 3s3g,),(8g = 1s4g)
#baaaaab= 6, baaaaba =5, baaabaa=4, baabaaa 3 2 1 = 31,



s = [0, 1, 2]
for i in range(3, 1001):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n] % 10007)



