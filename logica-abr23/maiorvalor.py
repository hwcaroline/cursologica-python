# Crie um pseudocódigo que recebe dois valores e exibe qual é o maior entre eles.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digte o segundo valor: '))


if (valor1 > valor2):
  print('O maior valor é o primeiro: ', valor1)
  print('Mais uma linha')
elif (valor1 < valor2):
  print('O maior valor é o segundo', valor2)
  print("mais")
else:
  print('Os valores são iguais!')

