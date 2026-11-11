
def fibonacci(n):
    if n <= 1:
        return n
    else:
        subSolution1 = fibonacci(n - 1)
        subSolution2 = fibonacci(n - 2)
        solution = subSolution1 + subSolution2
        return solution


numero = 10

for i in range(numero):
    print(fibonacci(i), end=" ")
