def mineiro(lista):
    result = []
    i = 0
    while i < qtd:
        # Primeiro elemento
        if i == 0:
            if lista[1] == 1:
                result.append(lista[i]+1)
            else:
                result.append(lista[i])

        # Último elemento
        elif i == (qtd-1):
            if lista[qtd-2] == 1:
                result.append(lista[i] + 1)
            else:
                result.append(lista[i])
        # Outros
        else:
            if lista[i+1] == 1 and lista[i-1] == 1:
                result.append(lista[i] + 2)
            elif lista[i+1] == 1 or lista[i-1] == 1:
                result.append(lista[i] + 1)
            else:
                result.append(lista[i])
        i += 1
    return result


qtd = int(input())
campo = []

for _ in range(0,qtd):
    mina = int(input())
    campo.append(mina)

if qtd == 1:
    print(mina)
else:
    result = mineiro(campo)
    for elem in result:
        print(elem)