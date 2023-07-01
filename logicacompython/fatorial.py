# Fatorial

numero = int(input("Digite o número que deseja calcular: "))

fatorial = 1

for i in (range(1, numero + 1)):
  fatorial = fatorial * i

print('O valor do fatorial é ', fatorial)