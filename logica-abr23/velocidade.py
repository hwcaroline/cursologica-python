# Escreva um programa que aplique uma multa caso a velocidade seja acima do limite de 80 km/h permitido:

# Até 10km/h por hora acima: multa leve
# Entre 11km/h e 20km/h: multa grave
# Acima de 20km/h: multa gravíssima

# O programa também deve verificar se a CNH está válida. Caso não esteja, deve aplicar multa gravíssima. 

velocidade = int(input('Digite a velocidade atual: '))
cnh_valida = input('Informe se a CNH está válida (s/n): ').lower()
vel_max_permitida = 80

if (cnh_valida == 'n'):
  print('Aplica multa gravíssima devido a CNH estar vencida!')
elif(cnh_valida == 's'):
  if (velocidade > vel_max_permitida) and (velocidade <= vel_max_permitida + 10):
    print('Aplica multa leve!')
  elif (velocidade >= vel_max_permitida + 11 ) and (velocidade <= vel_max_permitida + 20):
    print('Aplica multa grave!')
  elif (velocidade > vel_max_permitida + 21):
    print('Aplica multa gravíssima!')
  else:
    print('O carro está dentro da velocidade permitida!')
else:
  print('O valor digitado para CNH é inválido!')
  