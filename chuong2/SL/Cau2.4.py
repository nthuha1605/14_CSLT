import math
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
T=math.sqrt(x)
print("Dien tich=",T)

