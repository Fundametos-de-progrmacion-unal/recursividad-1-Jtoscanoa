def fibonacci(x):
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a + b
    return a