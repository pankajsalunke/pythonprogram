print('Enter number')
num=int(input())
f=0
for i in range(2,num):
    if(num%i==0):
        
        f=1
if f==0:
    print(num)
