num = 10
if num >10:
    print("more than 10")
else:
    print("less than 10")



num1 = int(input("შემოიყვანე რიცხვი"))
if num1 == 15:
    print("equal to 15")
else:
    print("not equal to 15")




text = input("შემოიყვანე სტრინგი")
if text == "group84":
    print("you are correct")
else:
    print("you are wrong")


for i in range(50, 101, 5):
    print(i)


for i in range(10):
    print("ილია გონგლაძე")


i = 20
while i  <= 50:
    print(i)
    i += 1

for i in range(0, 100):
    print(i)

i = 0
while i < 100:
    print(i)
    i += 1

for i in range(0, 101 ):
    print(i)


i = 0
while i <= 100:
    print(i)
    i += 1


for i in range(10, 21 ):
    print(i)


i = 10 
while i <= 20:
    print(i)
    i += 1


for i in range(100, 200, 5):
    print(i)


i = 100
while i <= 200:
    print(i)
    i += 5 


for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

number = float(input("შემოიყვანე რაიმე რიცხვი"))
if number > 0:
    print("ეს რიცხვი დადებითია")

elif number < 0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს რიცხვი ნულია")


age = int(input("შემოიყვანე შენი ასაკი"))
if age < 0:
    print("არასწორი ინფორმაცია")

elif age <= 12:
    print("ბავშვი ხარ")

elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")


elif age <= 64:
    print("ზრდასრული ხარ")

elif age >= 120:
    print("ხანში შესული ადამიანი ხარ")

else:
    print("გურუ ხარ ან ჯადოქარი")

number = float(input("შემოიყვანე პირველი რიცხვი"))
number1 = float(input("შემოიყვანე მეორე რიცხვი"))
number2 = float(input("შემოიყვანე მესამე რიცხვი"))
print("უდიდესი რიცხვია ",max(number, number1, number2) )



num = int(input("შემოიყვანე 1 დან 7 ამდე რიცხვი"))
if num >= 1:
    print("ორშაბათი")
elif num >=2:
    print("სამშაბათი")
elif num >= 3:
    print("ოთხშაბათი")
elif num >= 4:
    print("ხუთშაბათი")
elif num >= 5:
    print("პარასკევი")
elif num >= 6:
    print("შაბათი")
elif num >= 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")

num = int(input("შემოიყვანე რიცხვი"))
if num > 50:
    print(num * 5)
else:
    print(num ** 2)

text = input("შემოიყვანე პაროლი")
if text == "goa123":
    print("Password is correct!,")
else:
    print("incorrect password!")

num = int(input("შემოიტანე რიცხვი"))
num1 = 0
for i in range(1, num + 1 ):
    num1 += i
print("ჯამი არის  ", num1 )