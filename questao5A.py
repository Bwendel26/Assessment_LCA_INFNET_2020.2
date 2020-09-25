# -*- coding: utf-8 -*-

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