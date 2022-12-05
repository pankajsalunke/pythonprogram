a = [10,20,30,20,10,50,60,40,80,50,40]

print ("with duplicate value::",a)
duplicate = set()
original = []
for x in a:
    if x not in duplicate:
        original.append(x)
        duplicate.add(x)

print("after removing duplicate values::",duplicate)

