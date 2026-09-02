import random

print("jogo de adivinhação")
print("tente adivinhar um numero que estou pensando entre 1 e 100")
print("voce tem apenas 7 chances de acertar")

numero_secreto = random.randint(1, 100)
contador = 6
acertou = False

while contador > 0:
  tentativa = int(input("Digite o seu palpite: "))
  print("voce tem", contador, "tentativas")
  contador -= 1
  if tentativa == numero_secreto:
   print("Parabens voce acertou")
   acertou = True
  elif tentativa < numero_secreto:
    print("voce errou! o numero secreto é maior que", tentativa)
  else:
    print("voce errou! o numero secreto é menor que", tentativa)
if not acertou:
    print("voce perdeu! o numero secreto era", numero_secreto)  
else:
   print("voce acertou! o numero secreto era", 7 - contador + 1, "tentativa")