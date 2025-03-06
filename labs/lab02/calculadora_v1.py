# Calculadora em Python
# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

def main():
    print("\n******************* Calculadora em Python *******************")
    print("\nSelecione o número da operação desejada:\n")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    opcao = int(input("\nDigite sua opção [1|2|3|4]: "))
    
    if (opcao>=1) and (opcao<=4):
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        
        if (opcao == 1):
            print(f"\n{num1} + {num2} = {num1 + num2}")
        elif (opcao == 2):
            print(f"\n{num1} - {num2} = {num1 - num2}")
        elif (opcao == 3):
            print(f"\n{num1} * {num2} = {num1 * num2}")
        elif (opcao == 4) and (num2 != 0):
            print(f"\n{num1} / {num2} = {(num1 / num2):.2f}")
        else:
            print("\nNão é possível dividir por zero!")
    else:
        print("\nOpção inválida!")
        exit()

if __name__ == "__main__":
    main()