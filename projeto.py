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


def findCep(string): # Completa
    analisada = string
    index = 0
    k = 0
    while k != -1:
        k = analisada.find("-")

        # Confere se é telefone ou cep
        if analisada[k+4].isnumeric() or not analisada[k+1].isnumeric():
            analisada = analisada[k+1::]
        else:
            index = k
            break

    if index == 0:
        return "nao informado"

    i = index - 5
    cep = ""
    while analisada[i].isnumeric() or analisada[i] == "-":
        cep += analisada[i]
        i += 1

    return cep


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


def findPhone(string): # Completa
    indexes = []
    for i, l in enumerate(string):
        if l == "-":
            if string[i+4].isnumeric():
                indexes.append(i)

    phones = []
    for index in indexes:
        phone = ""
        i = index + 4
        while string[i].isnumeric() or string[i] == "-":
            phone += string[i]
            i -= 1
        phones.append(phone[::-1])

    if len(phones) > 1:
        phone = ""
        for i, k in enumerate(phones):
            if i == len(phones) - 1:
                phone += f"{k}"
            else:
                phone += f"{k}, "
        return phone
    else:
        return phones[0]


def findOwner(string): # Completa
    periodos = string.split(".")
    periodo = periodos[-2]

    index = 0
    owner = ""
    while index < len(periodo)-1:
        index += 1
        if periodo[index] == " " and not periodo[index+1].isupper():
            c = 0
            for l in owner:
                if l.isupper():
                    c += 1

            if c < 2:
                owner = ""
            else:
                break
        elif periodo[index] == " " and periodo[index+1].isupper():
            if owner[0].islower():
                owner = ""
            else:
                owner += periodo[index]
        elif periodo[index] == ",":
            continue
        else:
            owner += periodo[index]

    return owner

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
