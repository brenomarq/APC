# Lista de Dicionários - Questão 1
string = input()

letras = {
    "d": 0,
    "t": 0,
    "v": 0
}

for key in letras.keys():
    c = string.count(key)
    letras[key] = c

for key, item in letras.items():
    if item > 0:
        print(f"{key} {item}")
