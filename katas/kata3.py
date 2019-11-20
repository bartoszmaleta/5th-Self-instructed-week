def first_non_consecutive(arr):
    i = 1
    list_with_nonconsecutie = []
    for elem in arr:
        plus_one_elem = elem + 1
        if plus_one_elem != arr[i]:
            list_with_nonconsecutie.append(arr[i])
            if len(list_with_nonconsecutie) > 0:
                return list_with_nonconsecutie[0]
            else:
                return None
        i += 1
        if i == len(arr):
            return None


list_numbs = [1, 2, 3, 4, 5, 6, 7, 8]
func = first_non_consecutive(list_numbs)
print(func)

# list_numbs = [1, 2, 3, 4, 6, 7, 8]
# func = first_non_consecutive(list_numbs)
# print(func)
