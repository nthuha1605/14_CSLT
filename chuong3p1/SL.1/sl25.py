yrsOfservice=int(input('Nhap so nam kinh nghiem: '))
salary=int(input('Nhap muc luong: '))
bonus=0
if yrsOfservice<5:
    if salary <500:
        bonus=100
    else:
        bonus=200
else:
    bonus=700
print('Nonus amount: ',bonus)