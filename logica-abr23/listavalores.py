# Some os valores que são pares de uma lsita
# Multiplique os valores que são ímpares
# lista = [20, 9, 8, 7]

# Dica: O perador (%) é utilizado para obter o resto da divisão, caso o resto for zero, o valor é par, se for 1, o valor é ímpar.abs

listaValores = [20, 9, 8, 7]
totalSoma = 0
totalMultiplica = 1

for valor in listaValores:
  if (valor % 2 == 0):
    totalSoma = totalSoma = valor
  else:
    totalMultiplica = totalMultiplica + valor

print('O total da soma é: ', totalSoma)
print('O total da multiplicação é ', totalMultiplica)