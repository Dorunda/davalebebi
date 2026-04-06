print(5 > 3)
print(5 == 5)
print(5 > 3 and 10 > 7)
print(4 < 6 or 5 < 7)
print(2 > 5 or  6 > 10)

print(5 > 9 and 10 > 3)
print(10 > 15 and 12 > 3)
print(2 > 7 or 4 > 10)
print(3 > 8)
print(7 == 10)

#sequencing-არის თანმიმდევრობით რომ სრულდება მოქმედება 
#iteration-არის ერთი და იგივე მოქმედების მრავალჯერ განმეორება 
#selection-არის არჩევნის პროცესი
name = input("sheiyvane sheni saxeli")
surname = "Gongladze"
print(name)
print(surname)
#ეს იმიტომ არის სექვესინგი რომ name დან დაიწყებს ყოდის წაკითხვას შემდეგ surname შემდეგ ორივე პრინტი
#for loop-არის ციკლი რომელიც ერთი და იგივე კოდის განმეორებას ავტომატურად რამდენჯერმე ასრულებს
#range-ქმნის რიცხვების დიაპაზონს და მას გადაეცემა start step da stop
#for loop-მუშაობს იტერაციით და არის for ლუპში i 

car = "Mercedes"
for i in range(1):
    print(car)

surname = "Gongladze"
for i in range(101):
    print(surname)

mycolor = "Black"
for i in range(47):
    print(mycolor)

name = "i"
for i in range(33):
    print(name)

str1 = input("შემოიყვანე სტრინგ მნიშვნელობა")
str2 = input("შემოიყვანე სტრინგ მნიშვნელობა")
str3 = input("შემოიყვანე სტრინგ მნიშვნელობა")

num = int(input("შემოიყვანე ინტეჯერ ტიპის მნიშვნელობა"))
concadination = str1 + str2 + str3 + str(num)
print(concadination)


cvladi1 = "gamarjoba"
cvladi2 = 15
cvladi3 = 10.5
cvaladi4 = True
print(type(cvladi1))
print(type(cvladi2))
print(type(cvladi3))
print(type(cvaladi4))


num1 = int(input("შემოიყვანე რაიმე რიცხვი"))
num2 = int(input("შემოიყვანე რაიმე რიცხვი"))
num3 = int(input("შემოიყვანე რაიმე რიცხვი"))
num4 = int(input("შემოიყვანე რაიმე რიცხვი"))
print(num1 + num2 + num3 + num4)
