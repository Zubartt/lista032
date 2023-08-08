'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final do mês.
'''

# Solicita informações ao vendedor
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor no mês: "))

# Calcula a comissão (15% das vendas)
comissao = total_vendas * 0.15

# Calcula o salário completo (fixo + comissão)
salario_completo = salario_fixo + comissao

# Exibe os resultados
print(f"Nome do vendedor: {nome_vendedor}")
print(f"Salário fixo: R${salario_fixo:.2f}")
print(f"Comissão sobre vendas: R${comissao:.2f}")
print(f"Salário completo no final do mês: R${salario_completo:.2f}")