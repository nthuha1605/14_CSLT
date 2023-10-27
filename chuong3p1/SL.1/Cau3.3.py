tieuthu = float(input("Tieu thu="))
tiendien=0
if 1<=tieuthu<=100:
    tiendien = tieuthu * 550
elif tieuthu <= 150:
    tiendien = 100 * 550 + (tieuthu - 100) * 750
elif tieuthu <= 200:
    tiendien = 100 * 550 + 50 * 750 + (tieuthu - 150) * 950
else:
    tiendien = 100 * 550 + 50 * 750 + 50 * 950 + (tieuthu - 200) * 1350
vat = tiendien * 0.1
tong = tiendien + vat
print("Phai tra=", tong,sep='')