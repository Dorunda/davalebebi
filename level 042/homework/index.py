#1)
def remove_exclamation_marks(s):
    return s.replace("!", "")
#2)
def zero_fuel(a, b, c):
    return b * c  >= a
#3)
def distinct(seq):
    s = set()
    result = []
    for i in seq:
        if i not in s:
            s.add(i)
            result.append(i)
    return result
#4)
def whose_move(last_player, win):
    if win: 
        return last_player
    else:
        if last_player == "black":
            return "white"
        else:
            return "black"
#5)
def bmi(weight, height):
    index = weight / height ** 2
        
    if index <= 18.5:
        return "Underweight"
    elif index <= 25.0:
        return "Normal"
    elif index <= 30.0:
        return "Overweight"
    elif index > 30:
        return "Obese"
    