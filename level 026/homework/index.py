#1)
sia = [5, 6, 7, 8, 10]
total = 0
for i in sia:
    total += i

print("ჯამი:", total)

#2)
sia = [5, 6, 3, 4, 7]
num = 0
for i in sia:
    if i % 2 == 0:
        num += 1

print("სიაში ლუწების რაოდენობა არის:", num)

#3)
sia1 = [10, 20, 30, 40, 50]
min_num = sia[0]
max_num = sia[0]

for i in sia1:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i
print("მინიმუმი არის:", min_num )
print("მაქსიმუმი არის:", max_num)
#4)
sia2 = [10, 15, 30, 35, 40]
for i in sia2:
    if i % 2 != 0:
        print(i)
#5)
total = 0
while True:
    ricxvi = int(input("შემოიყვანე რიცხვი"))
    if ricxvi == 0:
        break
    total += ricxvi   
print(total)
#6)
while True:
    momxmarebeli = int(input("შემოიტანე რიცხვი:"))
    if momxmarebeli < 0:
        print("დასრულდა")
        break
#7)
while True:
    momxmarebeli1 = int(input("შემოიყვანე რიცხვი:"))
    if momxmarebeli1 % 5 == 0:
        print("იყოფა ხუთზე")
        break

#8)
count = 0

while True:
    momxarebeli2 = int(input("შემოიყვანე რიცხვი:"))
    count += 1
    if momxarebeli2 % 2 == 0:
        break

print("მცდელობები", count)

#9)
while True:
    momxarebeli2 = int(input("შემოიყვანე რიცხვი:"))
    if momxarebeli2 % 2 != 0:
        print("კენტია")
        break

#10)
while True:
    momxarebeli2 = int(input("შემოიყვანე რიცხვი:"))
    if momxarebeli2 < 0:
        continue
    if momxarebeli2 == 0:
        break
    print(momxarebeli2)

#11)
while True:
    momxarebeli2 = int(input("შემოიყვანე რიცხვები"))
    if momxarebeli2 < 0:
        continue
    if momxarebeli2 == 100:
        break
    print(momxarebeli2)
