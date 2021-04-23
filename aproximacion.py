def f(x):

    respuesta = 0 #Operación de inicio que cuenta como 1 -------------------------------------------------> 1 operacion

    # Constante que corre 1000 veces sin importar el valor de x ------------------------------------------> 1000 operaciones
    for i in range(1000):
        respuesta += 1

    # Loop que depende de x ------------------------------------------------------------------------------> x operaciones
    for i in range(x):
        respuesta += x

    # Loop dentro de loop equivalente a X al cuadrado pero hay 2 respuestas entonces se multiplica por 2 -> 2X^2
    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1
    
    return respuesta #Otra operación que cuenta como 1 ---------------------------------------------------> 1 operacion

    # 1 + 1000 + 1 + X + 2X^2
    # 1002 + X + 2X^2 --> Polinomio

    # Si x vale 1 entonces lo que más pesa es la constante:
    # 1002 + 1 + 2 = 1005

    # Cuanto más vale x relevante será el término de 2x^2
