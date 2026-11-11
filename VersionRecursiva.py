
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = 200
resultado = factorial(numero)

print("El factorial de", numero, "es:", resultado)

