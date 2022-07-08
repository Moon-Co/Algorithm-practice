money = int(input())
change = 1000-money
money_list = [500,100,50,10,5,1]
#380 = 620 = 500+100+10+10
count = 0
for i in money_list:
    if i <=change:
        count += change//i
        change = change%i
print(count)

