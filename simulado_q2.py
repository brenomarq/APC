# Simulado II - questão 2
# Beecrowd ID: 2633
while True:
    try:
        n = int(input())
        alimentos = {}
        for _ in range(0,n):
            nome, validade = input().split()
            validade = int(validade)
            alimentos[nome] = validade

        ordenado = sorted(alimentos.items(), key=lambda x: x[1])
        
        ans = ""
        for index, tupla in enumerate(ordenado):
            if index == len(ordenado)-1:
                ans += tupla[0]
            else:
                ans += tupla[0]+" "

        print(ans)

    except EOFError:
        break
