#1)
def remove_smallest(numbers):
    sia = list(numbers)   
    if sia:
        sia.pop(sia.index(min(sia)))
    return sia
#2)
def number(lines):
    result = []
    n = 1
    for line in lines:
        result.append(f"{n}: {line}")
        n += 1
    return result   
