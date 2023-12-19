import random
import os


def limpaTela():
    os.system('cls')

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
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta
        self.letras_usuario = [' ' for letra in self.palavra_secreta]
        self.letras_erradas = []
        self.letras_ditas = []

    # Método para verificar a letra
    def adivinhaLetra(self, letra):

        #verifica se a letra ja foi dita pelo usuario
        if letra in self.letras_ditas:
            return

        #verifica de o usuario digitou mais de 1 caracter, um número ou espaço em branco
        if len(letra) != 1 or letra.isnumeric() or letra == ' ':
            print('TENTATIVA INVÁLIDA!')
            return

        #adiciona na lista todas as letras citadas pelo usuário
        self.letras_ditas.append(letra)

        #adiciona somente as letras incorretas em uma lista
        if letra not in self.palavra_secreta:
            self.letras_erradas.append(letra)

        # Mostra a letra na posicao da palavra, alertado que o usuario acertou a letra
        for count, value in enumerate(self.palavra_secreta):
            if letra == value:
                self.letras_usuario[count] = letra

    # Método para verificar se o jogo terminou atraves dos erros ou se o jogador venceu
    def jogoAcabou(self):

        # se o jogador ja tiver errado mais de 6 letras ou acertado a palavra
        if len(self.letras_erradas) > 5 or self.jogadorVenceu():
            print(f'\nA palavra correta é {self.palavra_secreta}')
            return True

        return False

    # Método para verificar se o jogador venceu
    def jogadorVenceu(self):
        if ' ' not in self.letras_usuario:
            return True
        return False

    # Método para imprimir o board na tela e as letras já ditas
    def mostraStatus(self):
        print(board[len(self.letras_erradas)])
        print('Letras ja ditas: ', end=' ')
        for letra in self.letras_ditas: print(f'{letra}',end=' ')
        print('\n\t\t\t\t', end=' ')
        for letra in self.letras_usuario: print(f'[{letra}]', end=' ')


#gera palavra aleatoria na categoria fruta
def randomWord():
    banco_de_dados = ['BANANA', 'ABACAXI', 'LIMAO', 'MANGA', 'TOMATE', 'UVA', 'MELANCIA', 'CAJU', 'MORANGO', 'PERA', 'LARANJA']
    return random.choice(banco_de_dados)

def main():

    game = Hangman(randomWord())

    while not game.jogoAcabou():
        limpaTela()
        game.mostraStatus()
        letra = input('\n\nQual letra é o seu palpite?\t\t').upper()
        game.adivinhaLetra(letra)

    if game.jogadorVenceu():
        print('\nVOCÊ GANHOU! MUITO BEM!')
    else:
        print('\nVOCÊ NÃO GANHOU! SINTO MUITO!')

if __name__ == '__main__':
    main()

