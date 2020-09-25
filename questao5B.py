# -*- coding: utf-8 -*-
import csv

def variacaoPib(arquivo):
    """
        Função que verifica a variacao do pib, entre 2013 e 2020, de um dos países do arquivo:
        http://www.funag.gov.br/ipri/images/analise-pesquisa/tabelas/top15pib.pdf
        do FMI. Solicita um arquivo .csv como parâmetro.
    """

    with open(arquivo, newline="", encoding="utf-8") as csvfile:
        arquivoPibs = csv.DictReader(csvfile)
        for coluna in arquivoPibs:
            primeiroAno = float(coluna.get("2013").replace(",", "."))
            ultimoAno = float(coluna.get("2020").replace(",", "."))
            variacao = (ultimoAno * 100 / primeiroAno) - 100
            paisAtual = coluna.get("Pais")
            print("{}: Variação de {:.2f}% entre 2013 e 2020.".format(paisAtual, variacao))

variacaoPib("Assessment_PIBs.csv")