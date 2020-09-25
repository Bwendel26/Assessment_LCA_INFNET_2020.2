# -*- coding: utf-8 -*-

from questao5A import verificaPib
from questao5B import variacaoPib
from questao5C import  evolucaoPibGraph

#Main
arqv = "Assessment_PIBs.csv"
pais = str(input("Informe um país: "))
ano = int(input("Informe um ano entre 2013 e 2020: "))

verificaPib(arqv, pais, ano)
variacaoPib(arqv)
evolucaoPibGraph(arqv, pais)