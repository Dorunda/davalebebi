#1
sia = [1, 5, 6, 7, 7, 8]
total = 0 
for i in sia:
    total += i

num = total / len(sia)
print("ჯამი ", total )
print("საშუალო არითმეტიკული:", num)

#2
num = 15 

while True:
    number = int(input("შემოიტანე რაიმე რიცხვი:"))

    if number == num:
        print("გამოიცანი")
        break 

    else:
        print("სცადე კიდევ ერთხელ")

#3
while True:
    number = int(input("შემოიტანე რაიმე რიცხვი"))

    if number % 2 != 0:
        print("ეს კენტი რიცხვია")
        continue
    else:
        print("ეს ლუწი რიცხვია")
        break
    