# --------------------------------------------------------------------------- #
#           Analisador Léxico Simples em Python                               #
# --------------------------------------------------------------------------- #
#                                                                             #
#   Finalidade:  Define o analisador léxico                                   #
#                                                                             #
#   Equipe 3:                                                                 #
#   - Délis Albuquerque                                                       #
#   - Everton de Almeida                                                      #
#   - Gabriel Gomes                                                           #
#   - João Leonardo                                                           #
#   - Raul Santos                                                             #
#   - Roberta da Silva                                                        #
#                                                                             #
#                                                                             #
#   Licença: GNU GPL v3.0 - Consulte o arquivo LICENSE para mais detalhes.    #
#                                                                             #
# --------------------------------------------------------------------------- #

from dataclasses import dataclass


@dataclass(frozen=True)
class Token_types:
    TOK_NUM: str = "Número"
    TOK_OP: str = "Operador"
    TOK_PONT: str = "Pontuação"
    TOK_INDEF: str = "Não definido"


@dataclass
class Token:
    type: str
    value: int | str

    def __str__(self) -> str:
        return (
            f"Tipo: {self.type} {' ' * (13 - len(self.type))} -- Valor: {self.value}\n"
        )


class Lex:
    def __init__(self) -> None:
        self.list_token_types = []
        self._tokens_constants = {
            "+": "SOMA",
            "-": "SUB",
            "*": "MULT",
            "/": "DIV",
            "(": "PARESQ",
            ")": "PARDIR",
        }

    def _next_caracter(self) -> str:
        if self._position < len(self._code) - 1:
            self._position += 1
            return self._code[self._position]
        self._position += 1
        return ""

    def _concat_numbers(self, caracter) -> str:
        value = ""
        while caracter.isdigit():
            value += caracter
            caracter = self._next_caracter()
        return value

    def _search_tokens(self) -> None:
        self._position = 0
        while self._position < len(self._code):
            caracter = self._code[self._position]
            while caracter.isspace():
                caracter = self._next_caracter()
            if caracter.isdigit():
                value = self._concat_numbers(caracter)
                self.list_token_types.append(
                    Token(type=Token_types.TOK_NUM, value=int(value))
                )
            elif caracter in "+-*/":
                self.list_token_types.append(
                    Token(
                        type=Token_types.TOK_OP,
                        value=self._tokens_constants.get(caracter),
                    )
                )
                caracter = self._next_caracter()
            elif caracter in "()":
                self.list_token_types.append(
                    Token(
                        type=Token_types.TOK_PONT,
                        value=self._tokens_constants.get(caracter),
                    )
                )
                caracter = self._next_caracter()
            else:
                self.list_token_types.append(
                    Token(type=Token_types.TOK_INDEF, value=caracter)
                )
                caracter = self._next_caracter()

    def input(self, code: str) -> None:
        self.list_token_types.clear()
        self._code = code
        self._search_tokens()

    def __str__(self) -> str:
        string = "\n======= Análise =======\n"
        for token in self.list_token_types:
            string += str(token)
        return string
