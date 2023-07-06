# Lista de Recursividade - Questão 4
def JaChegou(n, s):
    if n == 0:
        return None
    else:
        print(s)
        JaChegou(n-1, s)
