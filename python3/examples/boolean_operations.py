# -*- coding: utf-8 -*-

number_1 = 3
number_2 = 4.5
number_3 = 3

name_1 = "Marcus"
name_2 = "Joe"
string_1 = "olá, Marcus"
string_2 = "olá, Joe"

result_1 = number_1 == number_2
print(result_1)

result_2 = number_1 != number_2
print(result_2)

result_3 = number_1 <= number_2
print(result_3)

result_4 = number_1 >= number_2
print(result_4)

result_5 = number_1 < number_2
print(result_5)

result_6 = number_1 > number_2
print(result_6)

result_7 = not (number_1 == number_2)
print(result_7)

result_8 = (number_1 == number_3) or (number_1 == number_2)
print(result_8)

result_9 = (number_1 == number_3) and (number_1 != number_2)
print(result_9)

result_10 = name_1 == name_2
print(result_10)

result_11 = name_1 != name_2
print(result_11)

result_12 = name_1 in string_1
print(result_12)

result_13 = name_1 in string_2
print(result_13)

result_14 = not (name_2 in string_2)
print(result_14)
