print('Enter three numbers ::')
a = int(input('first number:'))
b = int(input('second number:'))
c = int(input('third number:'))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triange is::",area)
