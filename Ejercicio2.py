def fibonacci(x):
    a, b = 1, 2
    for i in range(x): t = a, a = b, b=t+b
    return b