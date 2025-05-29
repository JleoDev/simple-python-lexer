---
# Analisador Léxico Simples em Python

Este projeto implementa um **analisador léxico** básico para expressões aritméticas, seguindo os princípios de um analisador léxico manual (sem a utilização de bibliotecas geradoras de analisadores como PLY ou Lex/Yacc). O objetivo é demonstrar a tokenização de números, operadores e pontuações em uma string de entrada.

---
## Funcionalidades

* **Análise Léxica Manual:** Implementado do zero para reconhecer e classificar tokens.
* **Reconhecimento de Tokens:** Identifica os seguintes tipos de tokens:
    * **Números:** Sequências de dígitos.
    * **Operadores:** `+`, `-`, `*`, `/`.
    * **Pontuação:** Parênteses `(` e `)`.
    * **Não Definido:** Quaisquer outros caracteres não reconhecidos.
* **Saída Formatada:** Apresenta os tokens reconhecidos de forma clara, indicando o tipo e o valor de cada um.

---
## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.

---
## Como Executar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado.

### Instalação das Dependências

Não há dependências externas complexas para este projeto. O código utiliza apenas funcionalidades nativas do Python.

1.  Clone este repositório (se aplicável, com base na estrutura de um repositório real):
    ```bash
    git clone https://github.com/JleoDev/simple-python-lexer.git
    cd simple-python-lexer
    ```

### Execução

1.  Navegue até o diretório raiz do projeto.
2.  Execute o script principal:
    ```bash
    python main.py
    ```
3.  O programa solicitará que você insira uma expressão para análise léxica no terminal.

---
## Uso

1.  Ao executar `main.py`, você verá a seguinte solicitação:
    ```
    Analise Lexica para Expressoes
    Expressao:
    ```
2.  Insira uma expressão aritmética no terminal, como por exemplo:
    * `10 + (25 * 5) / 2`
    * `30 - 7 * 4`
    * `(123 + 45)`
    * `abc + 1` (para ver tokens indefinidos)
3.  Pressione `Enter`. O analisador léxico processará a expressão e exibirá a lista de tokens reconhecidos:
    ```
    ======= Análise =======
    Tipo: Número         -- Valor: 10
    Tipo: Operador       -- Valor: SOMA
    Tipo: Pontuação      -- Valor: PARESQ
    Tipo: Número         -- Valor: 25
    Tipo: Operador       -- Valor: MULT
    Tipo: Número         -- Valor: 5
    Tipo: Pontuação      -- Valor: PARDIR
    Tipo: Operador       -- Valor: DIV
    Tipo: Número         -- Valor: 2
    ```

---
## Estrutura do Projeto

```
simple-python-lexer
├── lex.py
├── LICENSE
├── main.py
└── README.md
```

* **`lex.py`**: Contém a implementação da classe `Lex`, responsável pela lógica de tokenização. Define os tipos de tokens e o processo de leitura e classificação de caracteres.
* **`main.py`**: O script principal que interage com o usuário, recebe a expressão e utiliza a classe `Lex` para realizar e exibir a análise léxica.
* **`LICENSE`**: Arquivo de licença do projeto.
* **`README.md`**: Este arquivo, fornecendo informações sobre o projeto.

---
## Licença

Este projeto está licenciado sob a licença **GNU GPL v3.0**. Veja o arquivo `LICENSE` para mais detalhes.

---
