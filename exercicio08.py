'''
 Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.
 Sabe se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário
'''

# Solicita informações ao usuario
preco_custo = float(input("Digite o preço de custo do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo desejado: "))

# Calcula o valor de venda (preço de custo + acréscimo)
valor_venda = preco_custo * (1 + percentual_acrescimo / 100)

# Exibe o valor de venda
print(f"O valor de venda do produto é: R${valor_venda:.2f}")