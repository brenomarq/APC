# Lista de Recursividade - Questão 1
def imprimeTermos(n):
    if n <= 0:
        print(0)
    else:
        print(n)
        imprimeTermos(n-2)
