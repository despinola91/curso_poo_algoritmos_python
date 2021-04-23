import random

def busqueda_binaria(lista, start, end, objetivo):
    print(f'buscando {objetivo} entre {start} y {end - 1}')
    if start > end:
        return False


    medio = (start + end) // 2
    
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, end, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, start, medio - 1, objetivo)
    

if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')    