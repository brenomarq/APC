# Simulado II - questão 3
# Beecrowd ID: 2126

caso = 1
while True:
    try:
        subsequencia = input()
        entrada = input()
        tam_ent = len(entrada)
        tam_sub = len(subsequencia)
        indexes = []
        i = 0
        while i < tam_ent - tam_sub + 1:
            if entrada[i:i+tam_sub] == subsequencia:
                indexes.append(i)
            i += 1


        tam_indexes = len(indexes)

        if tam_indexes != 0:
            print(f"Caso #{caso}:")
            print(f"Qtd.Subsequencias: {tam_indexes}")
            print(f"Pos: {indexes[-1]+1}")
            print()
        else:
            print(f"Caso #{caso}:")
            print("Nao existe subsequencia")
            print()
        caso += 1
    except EOFError:
        break
