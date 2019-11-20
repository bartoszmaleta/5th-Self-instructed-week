# 1 = anane
# 2 = adak
# 3 = adak anane
# 4 = adak adak
# 5 = adak adak anane
# 6 = adak adak adak
# 7 = adak adak adak anane
# 8 = adak adak adak adak


def count_arara(n):
    if n == 1:
        answer = 'anane'
        return answer
    elif n == 2:
        answer = 'adak'
        return answer
    elif n == 3:
        answer = 'adak anane'
        return answer
    elif n == 4:
        answer = 'adak adak'
        return answer
    elif n == 5:
        answer = 'adak adak anane'
        return answer
    elif n == 6:
        answer = 'adak adak adak'
        return answer
    elif n == 7:
        answer = 'adak adak adak anane'
        return answer
    elif n == 8:
        answer = 'adak adak adak adak'
        return answer
    

func = count_arara(2)
print(func)

print('---------------------------------')


def count_arara2(n):
    odd = 'anane'
    even = 'adak'
    if n == 1:
        first_number = 'anane'
        return first_number
    elif n == 2:
        second_number = 'adak'
        return second_number
    elif n % 2 == 0 and n > 2:
        multiplier = int(n / 2)
        multiplier -= 1
        even_number = ''
        for i in range(multiplier):
            even_number += even
            even_number += ' '
        even_number += even
        return even_number

    elif n % 2 == 1 and n > 1:
        multiplier = int(n / 2)
        odd_number = ''
        multiplier -= 1
        for i in range(multiplier):
            odd_number += even
            odd_number += ' '
        odd_number += even
        odd_number += ' '
        odd_number += odd
        return odd_number            
        

func = count_arara2(1)
print(func)

func = count_arara2(2)
print(func)

func = count_arara2(7)
print(func)

func = count_arara2(9)
print(func)