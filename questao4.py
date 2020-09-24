# -*- coding: utf-8 -*-

# Importamos a coleção pytplot do módulo matplotlib.
# Documentação: https://matplotlib.org/tutorials/introductory/pyplot.html
# O trecho "as plt" significa que, neste programa, chamaremos o pyplot de plt.
import matplotlib.pyplot as plt

def rendimentoJurosCompostos(montanteInicial, percentualRendimento, aportePadrao, qtdDePeriodos):
    """
        função que calcula o rendimento de investimentos com base 
        em um aporte padrao, período de tempo, percentural de rendimento
        e montante inicial.
    """
    eixo_y_eixoRendimento = []
    eixo_x_eixoTemporal = []
    rendimentoAtual = 0
    montanteAtual = montanteInicial

    for index in range(0, qtdDePeriodos):
        rendimentoAtual = (percentualRendimento * montanteAtual / 100) + aportePadrao
        montanteAtual += rendimentoAtual
        periodoAtual = index + 1
        eixo_x_eixoTemporal.append(periodoAtual)
        eixo_y_eixoRendimento.append(montanteAtual)
        print("Após {} períodos(s), o montante será de R${:.2f}.".format(periodoAtual, montanteAtual))
    
    return eixo_x_eixoTemporal, eixo_y_eixoRendimento

def plotandoGraficoRendimento(eixos):
    plt.plot(eixos[0], eixos[1])
    plt.show()
    
#Main
montante = float(input("Valor inicial: R$ "))
percentualRendimento = float(input("Rendimento por período (%): "))
aportePadrao = float(input("Aporte a cada período: R$ "))
qtdPeriodos = int(input("Total de períodos: "))

eixos = rendimentoJurosCompostos(montante, percentualRendimento, aportePadrao, qtdPeriodos)
plotandoGraficoRendimento(eixos)