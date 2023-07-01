# Estrutura para while

ingressosVendidos = 10

while (ingressosVendidos < 20):
  ingressosVendidos = ingressosVendidos + 1
  print(ingressosVendidos)

print('Ingressos vendidos ', ingressosVendidos)

# Estrutura para coleções
# indice    0     1    2    3
valores = [800, 997, 1200, 497]
soma = 0

for valor in valores:
  soma = soma + valor
  print(soma, valor)

print('A soma destes valores é', soma)

# print(valores[2])
# print(valores.index(497))

paises = ["Brasil", "Venezuela", "Argentina"]

for pais in paises:
  print(pais)
