def fibonacci(x):
    a = 1
    b = 2
    print(a)
    print(b)
    for i in range(x):
        print(x+b)
        t = a
        a = b
        b=t+b