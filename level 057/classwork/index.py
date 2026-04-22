#1)
def divisors(n):
    count = 0
    
    for i in range(1, n + 1):
        if n % i ==0:
            count += 1
    return count
#2)
def longest(a1, a2):
    conc = a1 +  a2
    st = set(conc)
    srt =  sorted(st)
    return "".join(srt)
#3)
def min_max(lst):
    return [min(lst), max(lst)]
#4)
def sp_eng(sentence): 
    return "english" in sentence.lower()
#5)
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    