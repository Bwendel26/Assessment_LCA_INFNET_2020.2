# -*- coding: utf-8 -*-

# Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano. 

#     O programa solicita ao usuário o nome do país e o ano desejado.
#     Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 

#     País não disponível.
#     ou
#     Ano não disponível.

#     a depender do tipo de dado não encontrado. 

#     Exemplo de saída do programa:

#     Informe um país: Brasil
#     Informe um ano entre 2013 e 2020: 2020
#     PIB Brasil em 2020: US$2.35 trilhões.
import csv

def verificaPib(arquivo, pais, ano):
    """
        Função que verifica o pib de um dos países do arquivo:
        http://www.funag.gov.br/ipri/images/analise-pesquisa/tabelas/top15pib.pdf
        do FMI. Solicita um arquivo .csv como parâmetro, nome do país e ano do pib.
    """
    paisSelecionado = ""
    anoSelecionado = str(ano)
    pibPais = ""

    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        arquivoPibs = csv.DictReader(csvfile)
        for coluna in arquivoPibs:
            if coluna.get("País").lower() == pais.lower():
                paisSelecionado = coluna.get("País")
                pibPais = coluna.get(anoSelecionado)
                print("PIB {} em {}: US${} trilhões.".format(paisSelecionado, anoSelecionado, pibPais))
                break