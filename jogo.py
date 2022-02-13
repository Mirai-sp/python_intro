import adivinhacao
import forca

print("******************************")
print("*     Escolha o seu jogo     *")
print("******************************")

print("(1) Forca (2) Adivinhação")
jogo = 0
while ((jogo < 1) != (jogo > 2)):
    jogo = int(input('Qual o jogo: '))
    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        adivinhacao.jogar()
    else:
        print("Escolha a opção correta: 1 ou 2")