a = 3
b = 4
c = 5


# def is_triangle(a, b, c):
#     sum_of_a_and_b = a + b
#     sum_of_a_and_b_squared = sum_of_a_and_b * sum_of_a_and_b
#     a_squared = a * a
#     b_squared = b * b
#     c_squared = c * c
#     sum_of_a_and_c = a + c
#     sum_of_b_and_c = b + c
#     sum_of_a_squared_and_b_squared = a_squared + b_squared
#     pitagoras = sum_of_a_squared_and_b_squared

#     pitagoras2 = b_squared + c_squared
#     pitagoras3 = a_squared + c_squared

#     if sum_of_a_and_b < c and a > 0 and b > 0 and c > 0:
#         return False
#     # if sum_of_a_and_c > c and a > 0 and b > 0 and c > 0:
#     #     return True
#     # if sum_of_b_and_c > c and a > 0 and b > 0 and c > 0:
#         # return True
#     elif sum_of_a_and_c < b:
#         return False
#     elif sum_of_b_and_c < a:
#         return False
#     elif a <= 0 or b <= 0 or c <= 0:
#         return False
#     elif pitagoras > c:
#         return False
#     elif pitagoras2 > a:
#         return False
#     elif pitagoras3 > b:
#         return False


def is_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a): 
        return False
    else: 
        return True 


func = is_triangle(a, b, c)
print(func)

