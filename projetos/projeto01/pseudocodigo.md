## Pseudocódigo Jogo da Forca

1. Definir a lista de palavras possiveis
2. Escolher uma palavra aleatóriamente da lista
3. Criar uma lista vazia para armazenar as letras advinhadas
4. Definir o numero maximo de tentativas permitidas
5. Enquanto o numero de tentativas não atingir o limite máximo:
    1. Mostrar a plavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos
    2. Pedir ao jogador que adivinhe uma letra
    3. Verificar se a letra está na palavra
    4. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
    5. Se a letra adivinhada não esta na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"
    6. Verificar se todas as letras da palavra foram adivinhadas
    7. Se todas as letras foram adivinhadas, exibir a mensagem "Voce venceu!"
    8. Se o numero de tentativas restantes chegar a zero, exibir a mensagem "Você perde. a palavra era [palavra escolhida]" e encerrar o jogo
