# Lista de recursividade - Questão 2
def desarma(tempo):
    if tempo == 0:
        print("Cabum!!!! Explodiu")
    elif tempo == 1:
        print("Bomba desativada automaticamente!")
    elif tempo == 5:
        print("Seu tempo está acabando!")
        desarma(tempo-1)
    else:
        print(f"Atenção faltam {tempo} segundos...")
        desarma(tempo-1)


def explode(tempo):
    if tempo == 0:
        print("Cabum!!!! Explodiu")
    elif tempo == 1:
        print("Seja rápido. Falta 1 segundo")
        explode(tempo-1)
    elif tempo == 5:
        print("Seu tempo está acabando!")
        explode(tempo-1)
    else:
        print(f"Atenção faltam {tempo} segundos...")
        explode(tempo-1)


tempo_inicial = int(input())
recorde = int(input())

if recorde < tempo_inicial:
    explode(tempo_inicial)
else:
    desarma(tempo_inicial)
