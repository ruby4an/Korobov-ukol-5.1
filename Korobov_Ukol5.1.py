def factorial(n):
    counter = int(1)
    for i in range(0, n-1):
        x = counter*(n-i)
        counter = x
    print("Factorial equals to ", counter)


y = int(input("Load n: "))
factorial(y)
