def suma_digitos(n):
    s = str(n)
    suma = 0
    for digit in s:
        suma += int(digit)
    return suma