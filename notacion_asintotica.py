# Ley de la suma

def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n) -> Esta función tiene un crecimiento lineal.
# Si n crece en 10 entonces tardaremos 10 veces más.
# La función crece en O de n.



# Ley de la suma

def f2(n):

    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n^2) = O(n^2)
# La función crece en O de n cuadrado.
# Esta función es cuadrática.



# Ley de la multiplicación

def f3(n):

    for i in range(n):

        for j in range(n):
            print(i, j)

# O(n) * O (n) = O (n*n) = O(n^2)
# Crecimiento cuadrático



# Recursividad múltiple

def fibonacci(n):

    if n == 0:
        return 0
        
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2^n)
# Crecimiento exponencial