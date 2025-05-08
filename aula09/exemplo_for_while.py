# lst_valores = []

# for i in range(5):
#     num = int(input('Informe o número: '))
#     lst_valores.append(num)


# print(f'Os números são: {lst_valores}')

# lst_nomes = []
# resposta = ''

# while resposta != 'n':
#     nome = input('Informe o nome: ')
#     lst_nomes.append(nome)
#     resposta = input('Deseja cadastrar outro nome? ').lower()[0]


# print(f'Os nomes são: {lst_nomes}')

lst_nomes2 = []

while True:
    nome = input('Informe o nome: ')
    lst_nomes2.append(nome)
    resposta = input('Deseja cadastrar outro nome? ').lower()[0]

    if resposta == 'n':
        break


print(f'Os nomes são: {lst_nomes2}')
