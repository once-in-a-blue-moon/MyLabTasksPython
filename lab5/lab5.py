print("enter a, b: ")
a=int(input())
b=int(input())
for n in range(a, b, 1):
    print("n =", n)
    k=0; S=0
    for i in range(1, (n+1), 1):
        if (n % i == 0):
            k=k+1
            S=S+i
    print("number of dividers:", k, ". Sum of dividers:", S)