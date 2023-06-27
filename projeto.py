# Análise de anúncios sobre imóveis
def findModel(string): # Completa
    analisada = string.lower()
    if "alug" in analisada:
        return "Aluguel"
    else:
        return "Venda"


def findType(string): # Completa
    analisada = string.lower()
    if "casa" in analisada:
        return "Casa"
    else:
        return "Apartamento"

def findAdress(string) : # Completa
    variacoes = ["Avenida", "Rua"]
    index = 0
    for variacao in variacoes:
        k = string.find(variacao)
        if k != -1:
            index = k

    endereco = ""
    while not string[index].isnumeric():
        endereco += string[index]
        index += 1
    while string[index].isnumeric():
        endereco += string[index]
        index += 1

    return endereco
        

def findCep(string): # Refazer
    ...


def findArea(string): # Completa
    variacoes = ["metros quadrados", "m2"]
    index = 0
    for variacao in variacoes:
        k = string.find(variacao)
        if k != -1:
            index = k
    index -= 2

    if index < 0:
        return "nao informado"

    dimensao = ""
    while True:
        if string[index].isnumeric():
            dimensao += string[index]
            index -= 1
        else:
            break

    return dimensao[::-1]


def findPrice(string): # Completa
    variacoes = ["R$", "reais"]
    pontos = [",", "."]
    index = 0
    for variacao in variacoes:
        k = string.find(variacao)
        if k != -1:
            index = k

    if index == 0:
        return "nao informado"

    preco = ""
    if "R$" in string:
        index += 2
        while True:
            if string[index].isnumeric() or string[index+1].isnumeric():
                preco += string[index]
                index += 1
            else:
                break
        return preco
    else:
        index -= 2
        while True:
            if string[index].isnumeric() or string[index-1].isnumeric():
                preco += string[index]
                index -= 1
            else:
                break
        return preco[::-1]


def findPhone(string): # A consertar
    qtd = 0
    for index, letra in enumerate(string):
        if letra == "-":
            if string[index+1].isnumeric():
                qtd += 1

    k = findCep(string)
    if k != "nao informado":
        qtd -= 1

    reverso = string[::-1]
    phones = []
    for _ in range(0,qtd):
        phone = ""
        index = 0
        while not reverso[index].isnumeric():
            index += 1
        while reverso[index].isnumeric() or reverso[index] == "-":
            phone += reverso[index]
            index += 1
        reverso = reverso[index:]
        phones.append(phone[::-1])

    if len(phones) == 1:
        return phones[0]
    else:
        phones = phones[::-1]
        result = ""
        for index, phone in enumerate(phones):
            if index == len(phones) - 1:
                result += f"{phone}"
            else:
                result += f"{phone}, "
        return result

def findOwner(string): # Completa
    periodos = string.split(".")
    uteis = [periodos[-1], periodos[-2]]
    index = 0
    aux = 0
    for periodo in uteis:
        n = 0
        for letra in periodo:
            if letra.isupper():
                n += 1
        if n > aux:
            aux = n
        else:
            index += 1

    # Encontra onde começa o nome
    util = uteis[index]
    x = 0
    nome = ""
    if "Fal" in util:
        x += 3
        if "," in util:
            while not util[x].isupper():
                x += 1
            while util[x] != ",":
                nome += util[x]
                x += 1
        else:
            while not util[x].isupper():
                x += 1
            while x < len(util):
                nome += util[x]
                x += 1
    else:
        while not util[x].isupper():
                x += 1
        while x < len(util):
            nome += util[x]
            x += 1

    return nome

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
    cep = findCep(entrada)
    print(f"CEP: {cep}")

    # Encontra a área
    area = findArea(entrada)
    print(f"Area: {area}")

    # Encontra a área
    valor = findPrice(entrada)
    print(f"Valor: {valor}")

    # Encontra o(s) telefone(s)
    phone = findPhone(entrada)
    if len(phone) > 10:
        print(f"Telefones: {phone}")
    else:
        print(f"Telefone: {phone}")

    # Encontra o responsável
    owner = findOwner(entrada)
    print(f"Responsavel: {owner}")
