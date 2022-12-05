num = int(input('Enter a number:'))
sum=0
temp=num
while temp>0:
    r=temp%10
    sum=sum+r**3
    temp=temp//10
if num == sum:
    print("number is armstrong:",num)
else:
    print("number is not armstrong:",num)

