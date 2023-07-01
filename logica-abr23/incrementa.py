# Crie um programa que receba um número e o incrementa por 1 por 10 vezes

valor = int(input("Digite o valor a ser incrementado: "))

for i in range(10):
  valor = valor + 1 
  print(i, valor)

print("O valor final é ", valor)

#valorCom80 = valor + 0.8
#print(valorCom80)