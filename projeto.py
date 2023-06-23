# Análise de anúncios sobre imóveis
def findModel(string: str):
    analisada = string.lower()
    if "alug" in analisada:
        return "Aluguel"
    else:
        return "Venda"


def findType(string):
    analisada = string.lower()
    if "casa" in analisada:
        return "Casa"
    else:
        return "Apartamento"


def findAdress(string):
    variacoes = ["Avenida", "Rua"]
    index = 0
    for variacao in variacoes:
        k = string.find(variacao)
        if k != -1:
            index = k
    
    parte_1 = ""
    parte_2 = ""
    paradas = [",", "."]
    # Encontra a primeira parte do endereço
    while True:
        if string[index] in paradas:
            index += 1
            break
        elif string[index].isnumeric():
            break
        else:
            parte_1 += string[index]
        index += 1

    # Encontra a segunda parte do endereço
    while True:
        if string[index] in paradas:
            break
        else:
            parte_2 += string[index]
            index += 1

    return f"{parte_1},{parte_2}"

def findCep(string):
    ...


def findArea(string):
    variacoes = ["metros quadrados", "m2"]
    index = 0
    for variacao in variacoes:
        k = string.find(variacao)
        if k != -1:
            index = k

    if index == 0:
        return "nao informado"
    
    # Encontra o tamanho da área
    



def findPrice(string):
    ...


def findPhone(string):
    ...


def findOwner(string):
    ...

if __name__ == "__main__":
    entrada = input()

    # Encontra a modalidade
    modalidade = findModel(entrada)
    print(f"Modalidade: {modalidade}")

    # Encontra o tipo de imóvel
    tipo = findType(entrada)
    print(f"Tipo: {tipo}")

    # Encontra o endereço do imóvel
    endereco = findAdress(entrada)
    print(f"Endereco: {endereco}")

    # Encontra o Cep
    _ = findCep(entrada)
    print(f"CEP: {_}")

    # Encontra a área
    _ = findArea(entrada)
    print(f"Area: {_}")

    # Encontra a área
    _ = findPrice(entrada)
    print(f"Valor: {_}")

    # Encontra o(s) telefone(s)
    _ = findPhone(entrada)
    print(f"Telefone(s): {_}")

    # Encontra o responsável
    _ = findOwner(entrada)
    print(f"Responsavel: {_}")
