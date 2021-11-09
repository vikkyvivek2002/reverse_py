x = int(input())
sum = 0
while x>0:
    rem = x%10
    x=x//10
    sum = sum*10 + rem
print(sum)
