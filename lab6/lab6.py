import math
pi=math.pi
a=int(input("enter a = "))
b=int(input("enter b = "))
n=int(input("enter n = "))


def integral_1(k):
    sum=0
    h=pi/k
    i=1
    while(i<=k):
        x=i*h-h/2
        f=math.log(2+math.sin(x))
        sum=sum+f
        i+=1
    return (sum*h)

def integral_2(begin, end, k):
    sum=0
    h=(end-begin)/k
    i=1
    while(i<=k):
        x=begin+i*h-h/2
        f=math.pow(math.atan(x), 2)
        sum=sum+f
        i+=1
    return (sum*h)

def result(a, b, n):
    res=integral_1(n) + integral_2(a, b, n)
    return res

print("integral 1 is ", integral_1(n))
print("integral 2 is ", integral_2(a, b, n))
print("result is ", result(a, b, n))