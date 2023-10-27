a=float(input(''))
b=float(input(''))
c=float(input(''))
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print('Khong hop le')
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print('Tam giac vuong')
elif a==a and b==c and c==a:
    print('Tam giac deu')
else:
    print('Tam giac loai khac')
