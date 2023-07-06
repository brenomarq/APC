# Lista de Recursividade - Questão 6
def simples(a):
    if a != "repete":
        pass
    else:
        print("Olá! Vamos repetir!")
        simples(input())

simples(input())
