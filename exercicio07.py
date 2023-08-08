''' A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte um valor de uma compra,
 o número de prestações escolhidas e apresente como resultado o valor das prestações.'''

valor_compra = float(input("Informe o valor da compra: "))
numero = int(input("Informe o numero de prestações: "))

valor_prestacao = valor_compra / numero

print(f"O valor de cada prestação será de R${valor_prestacao:.2f}")