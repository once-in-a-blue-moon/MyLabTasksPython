a=float(input("Enter a = "))
if (a<=1):
    x=min(2*a, 0.95)
elif(a<25 and a>1):
    x=a/5
else: 
    x=a/25
e=0.0001
x1 = 0.0
while abs(x-x1)>e:
    x1=x
    x=0.8*x+a/(5*x**4)
    print(x)
x_fin=round(x, 4)
print("result: ", x_fin)
