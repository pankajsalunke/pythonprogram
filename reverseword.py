#a=input("Enter the String")
#A=""
#for i in a:
#    A=i+A
#print("String in reverse order",A)
#
def reverse(A):
    s = " "
    for i in A:
        s = i + s
    return s
A=input("Enter the String to reverse")
print("The original string is:",A)
print("The reverse string is:", reverse(A)) 

