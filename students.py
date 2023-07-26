'''
O intuito deste pequeno projeto é desenvolver um software básico que receba informações de um aluno
e armazene em um formato json, permitindo sua consulta posterior.
'''
import json
import os

def adicionar(dados: dict) -> None:
    with open(caminho) as f:
        data = json.load(f)

    data['alunos'].append(dados)
    json_object = json.dumps(data, indent=len(data))
    with open(caminho, "+w", encoding="utf-8") as arquivo:
        arquivo.write(json_object)


def consultar(nome: str) -> None:
    with open(caminho) as f:
        data = json.load(f)

    if len(data["alunos"]) == 0:
        os.system("clear")
        print("Não há nenhum dado para ser consultado.")
        return None

    dados = ""
    for aluno in data['alunos']:
        if nome == aluno['nome']:
            dados = aluno
    if dados:
        print(f"Aluno: {dados['nome']}, Matrícula: {dados['matricula']}")
        print(f"Sua média final é {dados['media']:.2f}")
        input()
        os.system("clear")
    else:
        print(f"O aluno(a) {nome} não foi encontrado(a).")
        input()
        os.system("clear")


def deletar(nome: str) -> None:
    with open(caminho) as f:
        data = json.load(f)

    if len(data['alunos']) == 0:
        os.system()
        print("Não há dados para serem consultados!")
        return None

    for index, aluno in enumerate(data['alunos']):
        if nome == aluno['nome']:
            del data['alunos'][index]

    json_object = json.dumps(data, indent=len(data))
    with open(caminho, "+w", encoding="utf-8") as arquivo:
        arquivo.write(json_object)

    print("Aluno(a) deletado(a) com sucesso!")


print("Bem-vindo, usuário!")
caminho = "dados.json"
while True:
    print("O que você deseja fazer?")
    print("[a]-adicionar [c]-consultar [u]-atualizar [d]-deletar [s]-sair")
    escolha = input("Digite sua opção: ")


    if escolha == "a":
        os.system("clear")
        nome = input("Digite o nome do aluno: ").capitalize()
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
        os.system("clear")
        consulta = input("Digite o nome do aluno: ").capitalize()

        consultar(consulta)

    elif escolha == "u":
        ...
    elif escolha == "d":
        deleta = input("Digite o nome do aluno: ")

        deletar(deleta)

    elif escolha == "s":
        os.system("clear")
        print("Obrigado por usar nosso programa!")
        break
    else:
        os.system("clear")
        print("Por favor, digite uma opção válida!\n")
