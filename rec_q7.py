# Lista de recursividade - Questão 7
def triangulo(x: int, size: int) -> None:
    if size == 1:
        print((" "*x)+"+")
    else:
        triangulo(x+1, size-2)
        print((" "*x)+("+"*size))
