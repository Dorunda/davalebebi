#1)
def abbrev_name(name):
    samharris = name.split()
    word1 = samharris[0]
    word = samharris[1]
    return f"{word1[0].upper()}.{word[0].upper()}"
#2)
import math
def litres(time):
    return math.floor(time * 0.5)
#3)
def find_average(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) /  len(numbers)
    
#4)
def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0
#5)
def divisors(n):
    result = []
    for i in range(2, n):
        if n % i == 0:
            result.append(i)      
    if len(result) == 0:
        return f"{n} is prime"
    else:
        return result
