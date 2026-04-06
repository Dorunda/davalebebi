#upper-გადაჰყავს დაბალი რეგისტრიდან მაღალ რეგისტრში სიტყვა
#lower-მაღალ რეგისტრიდან დაბალ რეგისტრში გადმოჰყავს
#capitalize-პირველ ასოს ადიდებს
#find-ეძებს სიმბოლოს და აბრუნდებს მის ინდექს

name = input("შემოიყვანე წინადადება")
print(name.lower())

name = input("შემოიტანე ელფოსტის მისამართი")
if "@" in name:
    print("True")
else:
    print("False")

wigni = input("შემოიტანე წიგნის დასახელება")
print(wigni.title())

winadadeba = input("შემოიყვანე წინადადება")
simbolo = input("შემოიყვანე სიმბოლო")
print(winadadeba.count(simbolo))


name = input("შემოიყვანე სიტყვა")
if name.isupper():
    print("სიტყვა უკვე დიდია")
else:
    print(name.upper())