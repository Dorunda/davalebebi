num = int(input("შემოიყვანე რაიმე რიცხვი: "))

if num > 0:
    if num % 2==0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")



num = 0
while num >= 0:
    num = int(input("შემოიყვანე რიცხვი:"))
    if num >= 0:
        print("Positive number entered")
    else:
        print("Negative number entered.Program stop")

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)



colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
num = int(input("შემოიყვანე ერთიდან 4 მდე რიცხვი:"))
print(colors[num])


animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)


colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
num = int(input("შემოიყვანე რიცხვი:"))
new_color = input("შემოიყვანე ფერი")
colors[num] = new_color
print(colors)

