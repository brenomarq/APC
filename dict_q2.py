# Lista de Dicionários - Questão 2
alunos = int(input())
notas = {}
iguais = []
for _ in range(alunos):
    aluno, nota = input().split(",")
    notas[aluno] = float(nota)

minha_nota = float(input())

for aluno, nota in notas.items():
    if nota == minha_nota:
        iguais.append(aluno)

iguais.sort()

if len(iguais) == 0:
    print("Você foi o único aluno com essa nota.")
elif len(iguais) == 1:
    print(*iguais)
else:
    colegas = ""
    for index, colega in enumerate(iguais):
        if index == len(iguais)-1:
            colegas += f"{colega}"
        else:
            colegas += f"{colega}/"
    print(colegas)
