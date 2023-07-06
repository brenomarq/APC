# Lista de Recursividade - Questão 3
def controle(n, c):
    if n <= 0:
        print(f"Parabens Julie! Voce tomou todos os {c} comprimidos!")
    elif c == 0:
        controle(n-1,c+1)
    else:
        print(f"Voce ja tomou {c} comprimidos, restam {n}.")
        controle(n-1,c+1)
