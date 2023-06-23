from projeto import findArea

caso1 = "Apartamento disponivel para aluguel na Avenida Sao Carlos, numero 542, CEP 13560-010. 140 metros quadrados, confortavel e espacoso. Falar no numero 99245-1777 com Jose Galdino."
caso2 = "Vendo um apartamento na Rua Alameda dos Crisantemos, 175, CEP 13566-550, proximo ao Bar do Toco, boa localizacao, arejado e com jardim secreto. Valor da venda a combinar. Falar com Rosane Minghim, no numero 99321-9746."
caso3 = "Apartamento para aluguel na Rua Jacinto Favoretto, 739, bairro Jardim Lutfalla, 87 m2. Valor: R$1.100,00 mensais. Necessário fiador morador de São Carlos. Contato: 99913-4532 ou 9231-8888. Geraldo Garcia Novaes."
caso4 = "Oportunidade unica. Vendo uma casa na Rua Episcopal, 45, super espacosa, 200 metros quadrados. O valor a vista eh 126.000,00 reais. Aceito permuta de terreno em Ribeirao Preto-SP. Telefone para contato e 9971-1056. Ricardo Campelo."

casos = [caso1, caso2, caso3, caso4]

for elem in casos:
    ans = findArea(elem)
    print(ans)
