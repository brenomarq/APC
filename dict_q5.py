# Lista de Dicionários - Questão 5
qtd = int(input())

corredores = []
for n in range(qtd):
    organizacao = input().split()
    produtos = []
    precos = []

    i = 1
    while i < len(organizacao):
        produtos.append(organizacao[i-1])
        precos.append(float(organizacao[i]))
        i += 2

    corredores.append(
        {
            "produtos": produtos,
            "precoMedio": sum(precos)/(len(precos))
        }
    )

selecao = int(input())-1

try:
    preco = corredores[selecao]["precoMedio"]
    produtos = str(corredores[selecao]["produtos"]).replace("'", '').replace('[', '').replace(']', '')
    print(f"No corredor {selecao+1} encontramos:")
    print(f"{produtos}")
    print(f"E o preço médio é {preco:.2f}.")

except IndexError:
    print("Esse corredor não existe no mercado.")
