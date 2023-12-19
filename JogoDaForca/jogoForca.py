import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, palavra_secreta, letras_certas, letras_erradas, letras_ditas):
        self.palavra_secreta = palavra_secreta
        self.letras_certas = letras_certas
        self.letras_erradas = letras_erradas
        self.letras_ditas = letras_ditas

    # Método para adivinhar a letra
    def adivinhaLetra(self):
        letra = input('\n\nQual letra é o seu palpite?\t\t').upper()

        #verifica se a letra ja foi dita pelo usuario
        if letra in self.letras_ditas:
            return
        #verifica de o usuario digitou mais de 1 caracter, um número ou espaço em branco
        if len(letra) != 1 or letra.isnumeric() or letra == ' ':
            print('TENTATIVA INVÁLIDA!')
            return

        letras_ditas.append(letra)

        #adiciona as letras erradas em uma lista
        if letra not in self.palavra_secreta:
            letras_erradas.append(letra)

        for count, value in enumerate(self.palavra_secreta):
            if letra == value:
                self.letras_certas[count] = letra




    # Método para verificar se o jogo terminou atraves dos erros ou se o jogador venceu
    def jogoAcabou(self):
        if len(self.letras_erradas) > 5:
            self.mostraStatus()
            print('\n******** VOCE PERDEU! *********')
            return False
        if self.jogadorVenceu():
            return False
        return True


    # Método para verificar se o jogador venceu
    def jogadorVenceu(self):
        if ' ' not in self.letras_certas:
            self.mostraStatus()
            print('\n******** VOCE GANHOU! MUITO BEM! *********')
            return True
        return False

    # Método para checar o status do game e imprimir o board na tela
    def mostraStatus(self):
        print(board[len(self.letras_erradas)])
        print('Letras ja ditas: ', end=' ')
        for letra in self.letras_ditas: print(f'{letra}',end=' ')
        print('\n')
        print('\t\t\t\t', end=' ')
        for letra in self.letras_certas: print(f'[{letra}]', end=' ')


#gera palavra aleatoria na categoria fruta
def GerarPalavra():
    banco_de_dados = ['BANANA', 'ABACAXI', 'LIMAO', 'MANGA', 'TOMATE', 'UVA', 'MELANCIA', 'CAJU', 'MORANGO', 'PERA', 'LARANJA']
    return banco_de_dados[random.randint(0, len(banco_de_dados)-1)]


palavra = GerarPalavra()

# variavel vazia que ira armazenar os acertos do usuario
letras_certas = []
for letra in palavra: letras_certas.append(' ')

letras_erradas = []
letras_ditas = []

usuario = Hangman(palavra, letras_certas, letras_erradas, letras_ditas)

while usuario.jogoAcabou():
    usuario.mostraStatus()
    usuario.adivinhaLetra()