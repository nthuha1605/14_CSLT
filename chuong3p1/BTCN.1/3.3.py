x = float(input('x='))
y = float(input('y='))
ch = input('Phep toan:')

if ch == '+':
    KQ = x + y
    print(x, '+', y, '=', round(KQ, 1), sep='')
elif ch == '-':
    KQ = x - y
    print(x, '-', y, '=', round(KQ, 1), sep='')
elif ch == '*' and (x != 0 and y != 0):
    KQ = x * y
    print(x, '*', y, '=', round(KQ, 1), sep='')
elif ch == '/' and (y != 0):
    KQ = x / y
    print(x, '/', y, '=', round(KQ, 1), sep='')
else:
    print('Khong hop le')