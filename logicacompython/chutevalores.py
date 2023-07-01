# Escreva um programa que gere um número aleatório de 1 a 10 e permita ao usuário chutar um número até que o valor aleatório seja igual ao chute

# Ao chutar, caso o valor esteja errado, informar se o valor está abaixo ou acima do chute
# O programa deve permitir que no máximo 3 chutes sejam tentados

import random

valorRandomico = random.randint(1,10)
acertou = False
tentativa = 1 

while (tentativa <= 3) and (acertou == False):
  valorInformado = int(input('Digite um valor de 1 a 10: '))
  tentativa += 1 #da no mesmo que fazer: tentativa = tentativa + 1
  
  if (valorInformado > valorRandomico):
    print('Seu chute está acima do valor randômico')
  elif (valorInformado < valorRandomico):
    print('Seu chute está abaixo do valor randômico')
  else:
    print('Você acertou!')
    acertou = True 
  
if (acertou == False):
  print('Você errou as 3 tentativas')

print('Valor randômico é: ', valorRandomico)
print('Valor do chute é: ', valorInformado)



