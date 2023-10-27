# ax+b=0
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
if a==0:
    if b==0:
        print("Phuong trinh co vo so nghiem")
    else:
        print('Phuong tring vo nghiem')
else:
    x=-b/a
    print("Phuong trinh co nghiem: ",x)

    
