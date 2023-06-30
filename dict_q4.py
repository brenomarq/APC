# Lista de Dicionários - Questão 4
qtd = int(input())
disciplina = {}

for _ in range(qtd):
    aluno = input().split()
    disciplina[aluno[0]] = (
        aluno[1],
        [float(x) for x in aluno[2:6]]
    )

selecao = input()

email = ""
media = 0
for aluno in disciplina:
    if aluno == selecao:
        email = disciplina[aluno][0]
        media = sum(disciplina[aluno][1])/4


if email == "":
    print(f"O aluno {selecao} não está na turma.")
else:
    print(f"Destinatário: {email}")
    if media >= 5:
        print(f"O aluno {selecao} foi aprovado com média {media:.2f}.")
    else:
        print(f"O aluno {selecao} foi reprovado com média {media:.2f}.")
