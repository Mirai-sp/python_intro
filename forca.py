import random

def jogar():
    imprime_boas_vindas()
    
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = carregar_palavra_acertada(palavra_secreta)
    print(letras_acertadas)

    enforcou   = False
    acertou    = False
    erros      = 0
    tentativas = 7

    #enquanto nao acertou e nao enforcou
    while (not enforcou and not acertou):
        chute = pede_chute()        

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            #print("Ops você errou ainda faltam {} tentativas.".format(tentativas-erros))

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprimir_mensagem_ganhador()        
    else:
        imprimir_mensagem_perdedor(palavra_secreta)


def imprime_boas_vindas():
    print("*****************************")
    print("* Bem vindo ao jogo da forca*")
    print("*****************************")

def carregar_palavra_secreta():
    # no list comprehension é possivel usar if como no exemplo
    # inteiros = [1,3,4,5,7,8,9]
    # pares = [x for x in inteiros if x % 2 == 0]
    
    #tuplas sao listas imutaveis para declara-las basta usar parenteses ao invez de chaves
    # a inicializacao da variavel letras_acertadas foi simplificada, pois poderia ter sido iniciado da seguinte forma
    # letras_acertadas = []
    # for letra in palavra_secreta:
    # letras_acertadas.append("_")
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().lower()
        palavras.append(linha)

    arquivo.close()

    numero_escolhido = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero_escolhido]
    return palavra_secreta

def carregar_palavra_acertada(palavra):
    return ["_" for letra in palavra] #aqui foi usado List Comprehension para inicializar a mesma

def pede_chute():
    chute = input("Qual letra? ")
    return chute.strip().lower()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprimir_mensagem_ganhador():
    print("Parabéns você acertou")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print("Infelizmente você errou")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

# testar se  foi chamado o arquivo diretamente, ou seja se nao foi via import
if (__name__ == '__main__'):
    jogar()