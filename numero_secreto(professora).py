import random

numero_secreto = random.randint(1, 1000)

print (numero_secreto)

num_tentativas = 0

print("Bem-vindo ao jogo de adivinhação!\nTente adivinhar o número secreto entre 1 e 1000.")

while True:
    palpite = int(input("Digite um número: "))
    num_tentativas =+ 1
    if (palpite == numero_secreto):
        print("👏👏👏👏👏👏👏👏")

    elif (palpite < numero_secreto):
        print("O número secreto é maior que o seu palpite.")

    else:
        print("O número secreto é menor que o seu palpite.")
