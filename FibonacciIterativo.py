
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        siguiente = a + b
        a = b
        b = siguiente


numero = 1000
fibonacci(numero)
