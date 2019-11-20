# def how_much_i_love_you(nb_petals):
#     one = 'I love you'
#     two = 'a little'
#     three = 'a lot'
#     four = 'passionately'
#     five = 'madly'
#     six = 'not at all'
#     nb_petals -= 1

#     list_with_petals = []
#     list_with_petals.append(one)
#     list_with_petals.append(two)
#     list_with_petals.append(three)
#     list_with_petals.append(four)
#     list_with_petals.append(five)
#     list_with_petals.append(six)

#     print(list_with_petals[nb_petals])


# num = 3
# func = how_much_i_love_you(num)
# print(func)

print('--------------------------')


def how_much_i_love_you(n):
    phrases = [
               'I love you',
               'a little',
               'a lot',
               'passionately',
               'madly',
               'not at all',
    ]

    return phrases[(n - 1) % len(phrases)]


num = 6
func = how_much_i_love_you(num)
print(func)
