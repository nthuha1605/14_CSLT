# print('M1=10')
# print('M2=20')
# print('M3=30')
# M1=10
# M2=20
# M3=30
M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
TT=int(input('S='))
if TT<=100:
    PT=M1*TT
    print('Phai tra=',PT,sep='')

elif 101<=TT<=150:
    PT=M1*100+(TT-100)*M2
    print('Phai tra=',PT,sep='')

elif 151<=TT:
    PT=M1*100+M2*50+M3*(TT-150)
    print('Phai tra=',PT,sep='')

    