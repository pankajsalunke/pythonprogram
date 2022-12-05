def pnum(n):
    sum = 0
    for x in range(1,n):
        if n%x == 0:
            sum = sum+x
    return sum == n

print(pnum(6))

