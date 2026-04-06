#1
#append-სიის ბოლოში ვამატებთ ნებისმიერ რამეს
#insert-სიაში ვამატებთ ნებისმიერ რამეს კონკრეტულ ინდექსზე 
#pop-სიაში არსებულ ელემენტს ვიღებთ ინდექსის საშუალებით
#2
sia1 = [15, 10, 20, 30, 40]
print(len(sia1))
#3
sia2 = []
for i in range(5):
    num = int(input("შემოიყვანე რიცხვი:"))
    sia2.append(num)
print(sia2)

#4
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)

#6
animals = ["dog", "cat", "elephant", "lion"]
animals.insert(2, "Monkey")
print(animals)
#7
sia3 = []
for i in range(3):
    name = input("შემოიყვანე სტუდენტის სახელი")
    sia3.append(name)
sia3.insert(0, "Teacher")
sia3.pop()
print(sia3)
