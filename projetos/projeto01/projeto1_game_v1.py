# Projeto 1 - Desenvolvendo um game em linguagem python - v1.0

# Import
import random
from os import system, name


#função para limpar a tela a cada execução
def limpar_tela() -> None:
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')


# Função
def main():
    limpar_tela()
    
    print('\nBem-vindo(a) ao jogo da forca!')
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras:list = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra da lista
    palavra:str = random.choice(palavras) 
    
    # List comprehension
    letras_descobertas:list = ['_' for letra in palavra]
    
    # Numero de chances
    chances:int = 6
    
    # Lista de letras erradas
    letras_erradas:list = []
    
    # Loop enquanto número de chances for mais do que zero
    while chances > 0: 
        # Print
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print(f"Letras erradas: {" ".join(letras_erradas)}")
        
        # Tentativa
        tentativa:str = str(input("\nDigite uma letra: ")).strip().lower()
        
        # Condicional
        if tentativa in palavra:
            index:int = 0
            
            for letra in palavra:
                if (tentativa == letra):
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        # Condicional
        if '_' not in letras_descobertas:
            print(f"\nVocê ganhou, a palavra era {palavra}")
            break
    
    # Condicional
    if '_' in letras_descobertas:
        print(f'\nVocê perdeu, a palavra era {palavra}')


# Bloco main
if __name__ == '__main__':
    main()
