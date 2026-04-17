#1)
def make_upper_case(s):
    return  s.upper()
#2)
def summation(num):
    return num * (num + 1) // 2

#3)
def to_alternating_case(string):
    text = ""
    for i in string:
        if i == i.upper():
            text += i.lower()
        elif i == i.lower():
            text += i.upper()
        else:
            text += i
    return text
#4)
def find_needle(haystack):
    index = haystack.index("needle")
    return "found the needle at position " + str(index)

#5)
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    