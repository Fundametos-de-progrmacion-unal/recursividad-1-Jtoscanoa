def fibonacci(x):
    a = 1
    b = 2
    for i in range(x):
        print(x+b)
        t = a
        a = b
        b=t+b
    return b