'''
O intuito deste pequeno projeto é desenvolver um software básico que receba informações de um aluno
e armazene em um formato json, permitindo sua consulta posterior.
'''
import json
import os

def adicionar(dados):
    with open(caminho) as f:
        data = json.load(f)
    
    data['alunos'].append(dados)
    json_object = json.dumps(data, indent=len(data))
    with open(caminho, "+w", encoding="utf-8") as arquivo:
        arquivo.write(json_object)

print("Bem-vindo, usuário!")
caminho = "dados.json"
while True:
    print("O que você deseja fazer?")
    print("[a]-adicionar [c]-consultar [u]-atualizar [d]-deletar [s]-sair")
    escolha = input("Digite sua opção: ")


    if escolha == "a":
        os.system("clear")
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite sua matrícula: ")
        notas = [float(input(f"Digite a {i+1}° nota: ")) for i in range(0,4)]
        media = sum(notas)/4

        dados = {
            "nome": nome,
            "matricula": matricula,
            "media": media
        }

        adicionar(dados)
        os.system("clear")
        print("Informações do aluno adicionadas com sucesso!")

    elif escolha == "c":
        ...
    elif escolha == "u":
        ...
    elif escolha == "d":
        ...
    elif escolha == "s":
        os.system("clear")
        print("Obrigado por usar nosso programa!")
        break
    else:
        os.system("clear")
        print("Por favor, digite uma opção válida!\n")
