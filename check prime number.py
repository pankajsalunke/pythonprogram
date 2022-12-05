num=int(input('Enter number :'))
f=0 
for i in range(2,num):
    if(num%i==0):
        f=1
        break
if f==0:
    print('num is prime')
else:
    print('num is not prime')
