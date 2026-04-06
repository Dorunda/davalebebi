#boolean-არის მონაცემთა ტიპი რომელის მნიშვნელობაც არის true false 
#binary code -არის ორობითი კოდი რომელიც მუშავდება მხოლოდ ნოლიანებით და ერთიანებით
#bool- არის რომელიც მხოლოდ იღებს ორ მნიშვნელობას true false   თუ პირობა არის სწორი გამოაქვს true თუ არარის სწორი გამოაქვს false
a = 10
b = 10
print(a == b)

num = int(input("შემოიყვანე ერთი რიცხვი"))
num1 = int(input("შემოიყვანე ერთი რიცხვი")) 
if  num > num1:
    print("პირველი რიცხვი მეტია მეორეზე")
elif num < num1:
    print("მეორე რიცხვი მეტია პირველზე")
else:
    print("რიცხვები ტოლია")



sityva = input("შემოიყვანე სიტყვა")
if sityva == "python ":
    print("სიტყვა ემთხვევა")
else:
    print("სიტყვა არ ემთხვევა")

num = int(input("შემოიყვანე რიცხვი"))
if num >  100:
    print("მეტია ")
else:
    print("ნაკლებია")





password = input("შემოიყვანე პაროლი")
if password == "Python123":
    print("სწორია")
else:
    print("არასწორია")



num1 = int(input("შემოიყვანე ერთი რიცხვი"))
num2 = int(input("შემოიყვანე მეორე რიცხვი"))
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)



s1 = input("შეიყვანე სიტყვა")
s2 = input("შეიყვანე სიტყვა")
s3 = input("შეიყვანე სიტყვა")
s4 = input("შეიყვანე სიტყვა")
s5 = input("შეიყვანე სიტყვა")
print(s1 + s2 +s3 +s4 +s5)




w1 = int(input("შემოიტანე რიცხვი"))
w2 = int(input("შემოიტანე რიცხვი"))
w3 = int(input("შემოიტანე რიცხვი"))
w4 = int(input("შემოიტანე რიცხვი"))
print((w1 + w2 +w3 +w4 ) / 4)




a = 10
b = 3.5
c = "ილია"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))



name1 = "ilia"
name2 = "gongladze"
print(num1 == num2 )



cvladi1 = "15"
cvladi2 = "10"
cvladi3 = "5"
cvladi4 = "3"
print(int(cvladi1) + int(cvladi2) + int(cvladi3) + int(cvladi4))




name = 5
name1 = 3
name2 = 2
print(str(name ) + str(name1) + str(name2))