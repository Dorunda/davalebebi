#1)
def count_sheeps(sheep):
    return sheep.count(True)
#2)
def sum_mix(arr):
    return sum(int(s) for s in arr)
#3)
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
#4)
def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"
#5)
def digitize(n):
    return [int(b) for  b in str (n)][::-1]
print(digitize(35231))