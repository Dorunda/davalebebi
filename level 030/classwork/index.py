name = input("შემოიყვანე შენი სახელი: ")
print(name.upper())

name1 = input("შემოიყვანე შენი სახელი")
print(name1.lower())

name2 = input("შემოიყვანე შენი სახელი")
print(name2.capitalize())

word = "gamarjoba"
word1 = input("შემოიყვანე რაიმე სიმბოლო")
if word1 in word:
    print(f"{word1}-{word.index(word1)}")
else:
    print("არ არის სიმბოლო")

name = "ilia"
print(len(name))

name = input("შემოიტანე სახელი")
if name.startswith("g"):
    print("იწყება g ასოთი")
else:
    print("არ იწყება g ასოთი")

name = input("შემოიყვანე შენი სახელი")
if name.endswith("l"):
    print("მთავრდება l ასოთი")
else:
    print("არ მთავრდება l ასოთი")