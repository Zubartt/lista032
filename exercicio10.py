'''
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores
'''
# Solicita o número total de eleitores
total_eleitores = int(input("Digite o número total de eleitores: "))

# Solicita o número de votos brancos, nulos e válidos
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Calcula os percentuais
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

# Apresenta os resultados
print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")