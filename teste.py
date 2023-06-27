from projeto import findCep

caso1 = "Tenho um apartamento para vender na Avenida Getulio Vargas, n. 387, na Vila Irene. O apartamento possui 132 metros quadrados, vazado, poente, 3 quartos, 2 banheiros, 1 cozinha e ar condicionado. Estou pedindo 200000,00 reais. Por favor, falar no numero 81234-9823 com Francisco Louzada."
caso2 = "Quero alugar uma casa completa, mobiliada, na Avenida Doutor Carlos Botelho, 1245, 13560-250, no Centro, proximo a padaria Guanabara. Valor e demais detalhes devem ser consultados no telefone 2124-2546 com Fernando Osorio."
caso3 = "Eu nao gostaria, mas estou endividado e preciso vender uma casa na Avenida Francisco Pereira Lopes, n. 7, no Cidade Jardim. A casa possui churrasqueira, piscina, 230 m2, 4 quartos, 1 suite, 3 vagas para carros, 1 sala e 1 quarto de servico. Tem um fusca velho guardado nos fundos, mas precisa quitar 20 parcelas vencidas do IPVA. O valor para venda eh 56234234 reais, mas faco desconto se quiser ficar com a minha sogra que soh sabe reclamar. Contato: 0000-0000. Falar com Illiarde Ubijara, tambem conhecido como jacare."
caso4 = "9876-5432. Vendo casa na Avenida da vida 13. 12345-678. 2.357,00 reais, 42 m2. Tem de ligar para o J J e perguntar mais detalhes."
caso5 = "Casa de 42 m2 para venda na Avenida da vida 13. 9876-5432 12345-678 por 2.357 reais. Tem de ligar para o J J J e perguntar mais detalhes."
caso6 = "12345-678 Avenida da vida 13, 42 m2 de casa para vender. 2357 reais. 9876-5432 09876-5432. Fale com J J."
caso7 = "9876-5432. Aluguel de apartamento na Rua da Lua 42, 12345-678. R$2.357,00, 13 metros quadrados. J J."
caso8 = "Alugo apartamento de 13 metros quadrados na Rua da Lua 42 9876-5432 12345-678 por R$2.357. Fale com J J J."
caso9 = "Rua da Lua 42 12345-678, 13 metros quadrados, apartamento para alugar. R$2357. Ligue dja! 9876-5432 ou 09876-5432. J J J."

casos = [caso1, caso2, caso3, caso4, caso5, caso6, caso7, caso8, caso9]

for caso in casos:
    ans = findCep(caso)
    print(ans)
