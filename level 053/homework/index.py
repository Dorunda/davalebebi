#1)
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()] 
#2)
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result
#3)
def divisible_by(numbers, divisor):
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] % divisor == 0:
            result.append(numbers[i])
        i += 1
    return result
#4)
def square_sum(numbers):
    return sum(x**2 for x in numbers)
#5)
def positive_sum(arr):
    return sum(max(0, x) for x in arr)