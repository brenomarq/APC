# Lista de Dicionários - Questão 3
ordem = input().split()
pedido = input().split()
produtos = {}
pedidos = {}

i = 1
while i < len(ordem):
    produtos[ordem[i-1]] = float(ordem[i])
    if i < len(pedido):
        pedidos[pedido[i-1]] = int(pedido[i])    
    i += 2

valor = 0
for produto in produtos:
    if produto in pedidos:
        valor += (produtos[produto] * pedidos[produto])

print(f"R$ {valor:.2f}")
