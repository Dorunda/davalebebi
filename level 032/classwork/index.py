#1
sia = [5, 6, 7, 8, 9, 10]
print(len(sia))


#2
sia1 = ["ილია", "ნიკა","ბაჩო", "ნიკოლოზი", "ნია", "მარიამი"]
name = input("შემოიყვანე სახელი:")
sia1.append(name)
print(sia1)



#3
sia2 = ["ნიკა", "ნიკოლოზი", "ნუგზარი", "დავითი", "მართა"]
sia2.insert(3, "Tarieli")
print(sia2)

#4
sia3 = [15, 10, 20, 30, 50, 60]
sia3.pop(4)
print(sia3)

#5
sia4 = ["ნიკოლოზი", "მახო", "მართა", "ნიკა", "გიო"]
sia4.remove("მახო")
print(sia4)

#6
momxmarebeli = input("შემოიყვანე სახელი")
sia5 = ["ნიკა", "გიორგი", "ილია", "ნიკოლოზი", "მართა", "დავითი"]
if momxmarebeli in sia5:
    print(sia5.index(momxmarebeli))
else:
    print("not index in list")

#7
sia6 = [5, 6, 7, 8, 9,]
for i in range(5):
    num = int(input("შემოიყვანე რიცხვი"))
    sia6.append(num)
print(sia6)

