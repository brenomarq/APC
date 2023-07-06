# Lista de Recursividade - Questão 5
def corrida(faltam, pneus, capacidade):
    if faltam == 0:
        print("A corrida chegou ao fim.")
    elif pneus == 0:
        print(f"Faltam {faltam} voltas, hora de trocar os pneus.")
        pneus = capacidade
        corrida(faltam, pneus, capacidade)
    else:
        corrida(faltam-1, pneus-1, capacidade)
