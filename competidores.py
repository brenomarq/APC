# Beecrowd ID: 2311
n = int(input())
competidores = {}
dificuldade = []
nomes = []

for _ in range(n):
    nome = input()
    nomes.append(nome)
    dificuldade.append(float(input()))
    pontuacao = [float(x) for x in input().split()]
    competidores[nome] = pontuacao

for elem in competidores.values():
    elem.sort()

for elem in competidores.values():
    del elem[0]
    del elem[-1]

i = 0
for nome in nomes:
    competidores[nome] = sum(competidores[nome]) * dificuldade[i]
    i += 1

for nome, pontuacao in competidores.items():
    print(f"{nome} {pontuacao:.2f}")
