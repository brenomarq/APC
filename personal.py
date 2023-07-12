'''
O intuito deste pequeno projeto é desenvolver um software básico que receba informações de um aluno
e armazene em um formato json, permitindo sua consulta posterior.
'''
import json
import os

print("Bem-vindo, usuário!")
caminho = "dados.json"
while True:
    print("O que você deseja fazer?")
    print("[a]-adicionar [c]-consultar [u]-atualizar [d]-deletar [s]-sair")
    escolha = input("Digite sua opção: ")


    if escolha == "a":
        os.system("clear")
        nome = input("Digite o nome do aluno: ")
        turma = input("Digite a turma: ")
        notas = [float(input()) for _ in range(0,4)]
        media = sum(notas)/4

        dados = {
            "nome": nome,
            "turma": turma,
            "media": media
        }

    elif escolha == "c":
        ...
    elif escolha == "u":
        ...
    elif escolha == "d":
        ...
    elif escolha == "s":
        ...
    else:
        os.system("clear")
        print("Por favor, digite uma opção válida!\n")
