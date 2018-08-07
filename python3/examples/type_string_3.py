# -*- coding: utf-8 -*-

string_1 = "Hi, "
string_2 = "name"
string_3 = str(65)
string_4 = str(3.14)

result_1 = string_1 + string_2
print(result_1)

result_2 = "number: " + string_3 + ", real: " + string_4
print(result_2)

result_3 = "number: {}, real: {}".format(string_3, string_4)
print(result_3)

result_4 = "number: {1}, real: {0}".format(string_4, string_3)
print(result_4)

result_5 = "number: {num}, real: {real}".format(real=string_4, num=string_3)
print(result_5)

result_6 = f"number: {string_3}, real: {string_4}"
print(result_6)

result_7 = f"number: {int(string_3)}, real: {float(string_4)}"
print(result_7)
