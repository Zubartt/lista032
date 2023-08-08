'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.
 Obs: Considere os anos com 365 dias e os meses com 30 dias.'''


anos = int(input("Informe o ano: "))
meses = int(input("Informe o mês: "))
dias = int(input("Informe o dia: "))

dias_vida = (anos*365) + (meses*30) + dias

print(f"Já se passaram {dias_vida} dias.")