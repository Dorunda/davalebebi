#1)
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i



#2)
def summation(num):
    return num * (num + 1) // 2
#3)
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 =="scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
#4)
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())
#5)
def format_names(names):
    return [name.capitalize() for name in names]