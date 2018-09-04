#!/usr/bin/env python3

def new_numeral_system_1(number):
    table = {chr(i): n for n, i in enumerate(range(65, 91, 1))}

    checks = [
        (char_1 is char_2, " + ".join([char_1, char_2]))
        for char_1 in table.keys()
        for char_2 in table.keys()
        if table[char_1] + table[char_2] is table[number]
    ]

    result = []

    for flag, content in checks:
        result.append(content)
        if flag:
            break

    return result

def new_numeral_system_2(number):
    table = {chr(i): n for n, i in enumerate(range(65, 91, 1))}

    checks = (
        (char_1 is char_2, " + ".join([char_1, char_2]))
        for char_1 in table.keys()
        for char_2 in table.keys()
        if table[char_1] + table[char_2] is table[number]
    )

    result = []

    for flag, content in checks:
        result.append(content)
        if flag:
            break

    return result

def new_numeral_system_3(number):
    table = {chr(i): n for n, i in enumerate(range(65, 91, 1))}

    checks = (
        (char_1 is char_2, " + ".join([char_1, char_2]))
        for char_1 in table.keys()
        for char_2 in table.keys()
        if table[char_1] + table[char_2] is table[number]
    )

    result = []

    for flag, content in checks:
        result.append(content)
        if flag:
            break

    return result
