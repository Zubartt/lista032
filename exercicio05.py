'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número,
a multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número
'''

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Cálculos
soma = num1 + num2
sub1 = num1 - num2
sub2 = num2 - num1
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

# Saída de resultados
print("Soma dos números:", soma)
print("Subtração do primeiro pelo segundo número:", sub1)
print("Subtração do segundo pelo primeiro número:", sub2)
print("Multiplicação entre os dois números:", multiplicacao)
print("Divisão do primeiro pelo segundo número:", divisao)
print("Resto da divisão do primeiro pelo segundo número:", resto)