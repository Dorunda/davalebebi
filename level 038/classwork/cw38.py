#name = "Hello its group 84"
#name = name.split(" ")
#print(name)
#for i in name:
#    if i == i[::-1]:
#        print(f"{i}  is palindrome!")
#    else:
#        print(f"{i} is not palindrome")


#name = '$'.join(name)
#print(name)


#sentance = "Hello world"
#splited = sentance.split(" ")
#joined = "$".join(splited)
#print(splited)
#print(joined)




sentance = input("გამარჯობა python:")
splited = sentance.split(" ")
print("დაშლილი წინადადება")
for splited in splited:
    print(splited)



sia = ['hi', 'hello', '84', '16']
symbol = input("$:")
result = symbol.join(sia)
print(result)