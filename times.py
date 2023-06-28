# Beecrowd ID: 2370
qtd_alunos, qtd_times = map(int, input().split())

alunos = {}
times = {}
new_alunos = {}
for _ in range(qtd_alunos):
    aluno, habilidade = input().split()
    alunos[aluno] = int(habilidade)

for k in range(qtd_times):
    times[f"time{k+1}"] = []

habilidades = [x for x in alunos.values()]
habilidades.sort(reverse=True)

for key, value in alunos.items():
    new_alunos[value] = key

l = 1
for i in habilidades:
    if l > qtd_times:
        l = 1
    
    jogador = new_alunos[i]
    times[f"time{l}"].append(jogador)
    l += 1

for h in range(1, qtd_times + 1):
    times[f"time{h}"].sort()

# Printar os valores
for i in range(1, qtd_times + 1):
    print(f"Time {i}")
    for elem in times[f"time{i}"]:
        print(elem)
    print()
