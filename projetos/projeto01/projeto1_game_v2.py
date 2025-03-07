# Projeto 1 - Desenvolvendo um game em linguagem python - v2.0

import random
from os import system, name


def limpar_tela() -> None:
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_hangman(chances):
    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


def main():
    limpar_tela()
    
    print('\nBem-vindo(a) ao jogo da forca!')
    print("Adivinhe a palavra abaixo:\n")
    
    palavras:list = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    palavra:str = random.choice(palavras) 
    
    letras_descobertas:list = ['_' for letra in palavra]
    
    chances:int = 6
    
    letras_erradas:list = []
    
    while chances > 0: 
        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print(f"Letras erradas: {" ".join(letras_erradas)}")
        
        tentativa:str = str(input("\nDigite uma letra: ")).strip().lower()
        
        if tentativa in palavra:
            index:int = 0
            
            for letra in palavra:
                if (tentativa == letra):
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        if '_' not in letras_descobertas:
            print(f"\nVocê ganhou, a palavra era {palavra}")
            break
    
    if '_' in letras_descobertas:
        print(f'\nVocê perdeu, a palavra era {palavra}')


if __name__ == '__main__':
    main()
