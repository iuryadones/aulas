# -*- coding: utf-8 -*-

name_1 = "Marcus"
name_2 = "Joe"
string_1 = "olá, Marcus"
string_2 = "olá, Joe"

if "Marcus" == name_2:
    print(string_1)
else:
    print("Desculpe, não entendo!")

if "Marcus" != name_2:
    print(string_1)
elif "Joe" == name_2:
    print(string_2)
elif "Marcus" == name_2:
    print(string_2)
else:
    print("Desculpe, não entendo!")
