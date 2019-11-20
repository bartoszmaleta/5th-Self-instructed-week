a = [1, 2, 3, 3, 3]
uniques = []
dups = []

for each in a:
    if each not in uniques:
        uniques.append(each)
    else:
        dups.append(each)
print("Unique values are below:")
print(uniques)
print("Duplicate values are below:")
print(dups)


print('---------------------------------')


# DICT

# a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
a = [2, 5, 34, 1, 22, 1]
d = {}
for elem in a:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1
        
print(d)

for elem in d.values():
    if elem > 1:
        print(d[elem])


print('---------------------------------')


def elimination(arr):
    duplicates = []
    uniques = []
    for elem in arr:
        if elem not in uniques:
            uniques.append(elem)
        else:
            duplicates.append(elem)
    
    if len(duplicates) == 0:
        return None
    
    return duplicates[0]


nums = [2, 5, 34, 1, 22, 1]
func = elimination(nums)
print(func)