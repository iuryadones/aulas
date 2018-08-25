"""

Your Informatics teacher at school likes coming up with new ways to help you
understand the material. When you started studying numeral systems, he
introduced his own numeral system, which he's convinced will help clarify
things. His numeral system has base 26, and its digits are represented by
English capital letters - A for 0, B for 1, and so on.

The teacher assigned you the following numeral system exercise: given a
one-digit number, you should find all unordered pairs of one-digit numbers whose
values add up to the number.

Example

For number = 'G', the output should be
newNumeralSystem(number) = ["A + G", "B + F", "C + E", "D + D"].

Translating this into the decimal numeral system we get: number = 6, so it is
["0 + 6", "1 + 5", "2 + 4", "3 + 3"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] char number

A character representing a correct one-digit number in the new numeral system.

Guaranteed constraints:
'A' ≤ number ≤ 'Z'.

[output] array.string

An array of strings in the format "letter1 + letter2", where "letter1" and
"letter2" are correct one-digit numbers in the new numeral system. The strings
should be sorted by "letter1".

Note that "letter1 + letter2" and "letter2 + letter1" are equal pairs and we
don't consider them to be different.

"""

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

    print(result)

    return result

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

    print(result)

    return result


def test_time(func):
    import time

    init = time.time()
    func()
    end = time.time()
    print(f"function: {func.__name__}\ntime: {end-init}\n")


def run_1():
    number = "G"
    new_numeral_system_1(number)

def run_2():
    number = "D"
    new_numeral_system_2(number)

def main():
    test_time(run_1)
    test_time(run_2)

if __name__ == "__main__":
    main()
