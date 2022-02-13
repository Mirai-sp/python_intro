import random

def jogar():
    print("*****************************")
    print("Bem vindo ao jogo adivinhação")
    print("*****************************")

    numero_secreto = random.randrange(1, 101)
    numero_tentativas = 0
    tentativa = 1
    nivel = 0
    pontos = 1000

    while ((nivel < 1) != (nivel > 3)):
        print('Escolha a dificuldade')
        print('(1) Fácil (2) Médio (3) Difícil')
        nivel = int(input('Defina o nível: '))
        if ((nivel < 1) != (nivel > 3)):
            print('Escolha entre 1, 2 ou 3.')

    if (nivel == 1):
        numero_tentativas = 20
    elif (nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    #while (tentativa <= numero_tentativas):
    for tentativa in range(1, numero_tentativas + 1):
        chute = int(input("Digite o seu numero entre 1 e 100: "))

        print("Você digitou ", chute)

        if (chute < 1 != chute > 100):
            print("Digite um número entre 1 e 100, verifique!")
            print("Você ainda tem {} de {} tentativas" . format(numero_tentativas - tentativa, numero_tentativas))
            continue    

        if (chute == numero_secreto):
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print("Voce errou, o seu chute foi maior que o número secreto!")
            elif (chute < numero_secreto):
                print("Voce errou, o seu chute foi menor que o número secreto!")            
            
            # if ternario para fazer subtracao de pontos de forma correta no caso poderia ter usado abs para deixar o calculo mais simples mas deixarei para estudo
            pontos = pontos - (numero_secreto - chute if numero_secreto >= chute else chute - numero_secreto)
            #pontos = pontos - (abs(numero_secreto - chute))
            print("Você ainda tem {} de {} tentativas" . format(numero_tentativas - tentativa, numero_tentativas))
    #        tentativa = tentativa + 1
    #        print("Voce ainda tem", numero_tentativas, "tentativas")        

    print("Fim do jogo")

# testar se  foi chamado o arquivo diretamente, ou seja se nao foi via import
if (__name__ == '__main__'):
    jogar()