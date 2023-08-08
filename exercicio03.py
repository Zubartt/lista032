'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros).
Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

# Pergunta ao usuario seu peso e a sua altura
peso_quilos = float(input("Digite o seu peso em quilos: "))
altura_metros = float(input("Digite a sua altura em metros: "))

# Calcula o peso e a altura
peso_gramas = peso_quilos * 1000
altura_centimetros = altura_metros * 100

# mostra os resultados
print(f"Seu peso em gramas é: {peso_gramas}g")
print(f"Sua altura em centímetros é: {altura_centimetros}cm")