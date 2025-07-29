# --------------------------------------------------------------------------- #
#           Analisador Léxico Simples em Python                               #
# --------------------------------------------------------------------------- #
#                                                                             #
#   Finalidade:  Define interface CLI para o analisador                       #
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

from lex import Lex

lex = Lex()
code = input("Analise Lexica para Expressoes\nExpressao: ")
lex.input(code)
print(lex)
