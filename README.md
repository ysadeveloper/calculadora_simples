# Calculadora Simples em Python

Uma calculadora de linha de comando simples desenvolvida em Python. Este projeto é ideal para iniciantes que querem entender os conceitos básicos de entrada/saída de dados, estruturas condicionais (`if/elif/else`), loops (`while`) e tratamento de erros (`try/except`).

---

### Funcionalidades

A calculadora suporta as seguintes operações:
- **Adição** (`+`)
- **Subtração** (`-`)
- **Multiplicação** (`*`)
- **Divisão** (`/`)

---

### Como Usar

1.  **Pré-requisito:** Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).

2.  **Execute o script:** Abra o terminal ou prompt de comando, navegue até o diretório onde o arquivo `calculadora.py` está salvo e execute o seguinte comando:

    ```bash
    python calculadora.py
    ```

3.  **Siga as instruções:** O programa irá pedir para você digitar o primeiro número, a operação e o segundo número.

    ```
    --- Calculadora Simples ---
    Digite o primeiro número: 10
    Digite a operação (+, -, *, /): +
    Digite o segundo número: 5
    O resultado é: 15.0
    ```

4.  **Continuar ou sair:** Após cada cálculo, o programa perguntará se você deseja fazer outro cálculo. Digite `s` para continuar ou `n` para sair.

---

### Estrutura do Código

-   **`calculadora()`**: Função principal que contém o loop da calculadora.
-   **`while True`**: Permite que a calculadora continue em execução até que o usuário decida sair.
-   **`try...except`**: Trata erros, como a entrada de valores não numéricos (`ValueError`) ou a divisão por zero.
-   **`.lower()`**: Usado para converter a entrada do usuário para minúsculas, tornando a resposta não sensível a maiúsculas e minúsculas (por exemplo, `s` ou `S` para continuar).

---
