def cadasrar_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = float(input('Informe o valor da venda: '))

        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lista_vendedor_vendas.append(pessoa)


def calcula_total_media():
    tot = 0
    for pessoa in lista_vendedor_vendas:
        tot += pessoa['Valor']
    med = tot/len(lista_vendedor_vendas)

    return tot, med


def calcula_maior_venda():
    mv = 0
    v = ''
    for i in lista_vendedor_vendas:
        if i['Valor'] > mv:
            mv = i['Valor']
            v = i['Nome']
    return mv, v


def busca_vendedor(nm_vend):
    nv = ''
    for nm in lista_vendedor_vendas:
        if nm['Nome'] == nm_vend:
            nv = nm_vend
            break
    return nv


#   Def1    #
lista_vendedor_vendas = []

qtd = int(input('Quantas pessoas? '))
cadasrar_pessoa(qtd)

print(lista_vendedor_vendas)

#   Def2    #
total, media = calcula_total_media()

print(f'Valores Total de vendas R${total:.2f} e média de vendas R${media:.2f}')

#   Def3    #
maior_venda, maior_vendedor = calcula_maior_venda()

print(f'Maior valor de venda R${maior_venda}, vendedor {maior_vendedor}')

#   Def4    #
nm_vend = input('Busque o vendedor: ')
nome_vendedor = busca_vendedor(nm_vend)

if nome_vendedor:
    print(f'O vendedor é: {nome_vendedor}')
else:
    print('Vendedor não encontrado.')
