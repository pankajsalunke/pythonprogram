A={71:"ram",98:"sham",1:"jay",3:"shri"}
sorted_values = sorted(A.values())
sorted_dict = {}

for i in sorted_values:
    for k in A.keys():
        if A[k] == i:
            sorted_dict[k] = A[k]

print(sorted_dict)
