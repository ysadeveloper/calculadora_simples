def calculadora():
    """
    Esta função implementa uma calculadora simples.
    Ela pede ao usuário para inserir dois números e uma operação,
    e então imprime o resultado.
    """
    print("--- Calculadora Simples ---")

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
            else:
                print("Operação inválida. Por favor, use +, -, *, ou /.")
                continue

            print(f"O resultado é: {resultado}")
            
            # Pergunta se o usuário quer fazer outro cálculo
            continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    print("Obrigado por usar a calculadora!")

# Chama a função para iniciar a calculadora
calculadora()