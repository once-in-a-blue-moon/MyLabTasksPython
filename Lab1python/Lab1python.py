
import math
a = float(input("Ввести кут а: "))
b = float(input("Ввести кут b: "))
c = float(input("Ввести кут c: "))
r = float(input("Ввести радіус вписаного кола: "))
n = a + b + c
if n==180 and a>=0 and b>=0 and c>=0 and r>=0:
    a = math.radians(a)
    b = math.radians(b)
    c = math.radians(c)
    sina = math.sin(a)
    sinb = math.sin(b)
    sinc = math.sin(c)
    stor1 = float(2*r*sina)
    stor2 = float(2*r*sinb)
    stor3 = float(2*r*sinc)
    print("Сторона 1 = ", stor1, "см")
    print("Сторона 1 = ", stor2, "см")
    print("Сторона 1 = ", stor3, "см")
else: print("ERROR! Incorrect data")
