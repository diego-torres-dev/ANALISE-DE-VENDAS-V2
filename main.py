# Lista de tuplas com informações de vendas
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# Armazena o valor da receita bruta com iPhones
receita_iphone = 0

# Percorre a lista de tuplas
for venda in vendas:
    # Desempacota a tupla desta iteração
    data, produto, cor, memoria, qtde, preco = venda

    # Verifica se a venda ocorreu em 20/08/2020 e se o produto era iPhone
    if data == "20/08/2020" and "iphone" in produto:
        receita_iphone += qtde * preco

receita_iphone = "{:_.2f}".format(receita_iphone)
receita_iphone = receita_iphone.replace(".", ",").replace("_", ".")

print("Receita com vendas de iPhone no dia 20/08/2020: R${}.".format(receita_iphone))

produto_mais_vendido = ""
qtde_produto_mais_vendido = 0

for venda in vendas:
    data, produto, cor, memoria, qtde, preco = venda
    if data == "21/08/2020":
        if qtde > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = qtde

print("Produto mais vendido em 21/08/2020 foi o {}, com {} unidades vendidas.".format(
    produto_mais_vendido, qtde_produto_mais_vendido))
