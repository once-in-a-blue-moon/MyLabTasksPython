print("enter a, b: ")
a=int(input())
b=int(input())
if (a>b):
    print("b must be > a")
else:
    for n in range(a, b+1, 1):
        if (n>0):
            print("n =", n, ". dividers are: ")
            k=0; S=0
            for i in range(1, (n+1), 1):
                if (n % i == 0): 
                    k=k+1
                    S=S+i
                    print(i)
            print("number of dividers:", k, ". Sum of dividers:", S)