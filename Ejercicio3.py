def suma_digitos(n):
    s = str(n)
    suma = 0
    for i in s:
        suma += int(i)
    return suma