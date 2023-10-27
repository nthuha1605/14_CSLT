# ax2+bx+c=0
import math
a=float(input('Nhap a: '))
b=float(input('Nhap b: '))
c=float(input('Nhap c: '))
dt=b*b-4*a*c
if dt>0:
    x1=(-b+math.sqrt(dt))/2*a
    x2=(-b-math.sqrt(dt))/2*a
    print("Phuong tring co hai nghiem: ",x1, "va " ,x2)
elif dt==0:
    x=-b/(2*a)
    print("Phuong trinh co nghiem: ",x)
else:
    print('Phuong trinh vo nghiem')

