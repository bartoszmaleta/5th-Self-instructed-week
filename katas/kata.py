
# def find_multiples(integer, limit):
    
#     list_with_numbers = []
#     list_with_numbers.append(integer)
#     multiplier = 2

#     while integer <= limit:
#         new_integer = integer * multiplier
#         list_with_numbers.append(new_integer)
#         multiplier += 1
#         if new_integer == limit:
#             break
#     return list_with_numbers    


def find_multiples(integer, limit):
    list_numbers = []
    for i in range(integer, limit + 1, integer):
        # if i <= limit:
        list_numbers.append(i)
    
    return list_numbers
    

print(find_multiples(5, 25))