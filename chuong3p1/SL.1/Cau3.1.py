a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
min=a
max=a
if b>max:
    max=b
elif b<min:
    min=a
if c >max:
    max=c
elif c<min:
    min=c
print('SLN=',max,sep='')
print('SBN=',min,sep='')

