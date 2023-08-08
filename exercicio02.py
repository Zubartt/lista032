'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos minutos atuais.
 Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
'''

# Pergunta ao usuario as horas
horas_atuais = int(input("Informe as horas atuais (formato 24h): "))

# Pergunta ao usuário os minutos
minutos_atuais = int(input("Informe os minutos atuais: "))

# Calcula quantos minutos já se passaram no dia
minutos_passados = horas_atuais * 60 + minutos_atuais

# mostra o resultado
print(f"Já se passaram {minutos_passados} minutos desde às 00:00h deste dia.")