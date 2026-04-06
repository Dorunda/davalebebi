#def greet(name):
#    print("Hello" + name)
#greet("ILIA")

#def getsum(Sia):
 # res = 0
#  for i in Sia:
 #   res += int(i)
 #   return res
  

#print(getsum([1, 2, 3 , 4,  5, '5', '6' '10']))

#def getready(time, status):
#    return time,  status
#print(getready(15, 20))




def getsum(a, b, c, d, e):
   getsum = ( a + b + c + d + e) / 5
   print(getsum)
   getsum(2, 4, 5, 6, 10)


def greet(name = "Guest"):
  return f"Say Hi {name}"
print(greet("Ilia"))  

def name_to_upper(name):
   return name.upper()
result = name_to_upper("ilia")
print(result)