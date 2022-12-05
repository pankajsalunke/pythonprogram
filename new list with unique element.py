def list1(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
l1 = ([1,2,2,33,33,4,3,5,6,7,6,7,8,9,2])
print('original list is :',l1)

print('new list is :',list1(l1))

