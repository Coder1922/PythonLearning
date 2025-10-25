def factorial(n):
    c=1
    for i in range(1,n+1):
        c*=i
    print(c)
    
n=int(input("Enter a number: "))
factorial(n)
