# -*- coding: utf-8 -*-

def saudeFinanceira(rendaMensal, gastosMoradia, gastosEducacao, gastosTransporte):
    """
        Funcao que calcula sua saude financeira com base em dados do BTG Pactual
        Com base em seus gastos por renda serem apenas 30% de moradia, 20% de educacao e
        15% em transporte.
    """
    #Variaveis 
    totalGastos = gastosMoradia + gastosEducacao + gastosEducacao
    percentualTotalGastos = totalGastos * 100 / rendaMensal
    percentualMoradia = gastosMoradia * 100 / rendaMensal
    percentualEducacao = gastosEducacao * 100 / rendaMensal
    percentualTransporte = gastosTransporte * 100 / rendaMensal
    resultadoPadraoString = "Seus gastos com {} comprometem {:.1f}% na sua renda total. O máximo recomendado é de {}%"
    resultadoPadraoString.replace("\n", " ") #impedindo quebra de linha.
    resultadoVariavelString = ""
    
        #listas de controle
    controleResultados = []
    nomeDoGasto = ["moradia", "educação", "transporte"]
    maxPercentualPorGasto = [30, 20, 15]
    gastoMaxRecomendado = [(rendaMensal / 100) * maxPercentualPorGasto[0], (rendaMensal / 100) * maxPercentualPorGasto[1], (rendaMensal / 100) * maxPercentualPorGasto[2]]
    listaPercentualPorGasto = [percentualMoradia, percentualEducacao, percentualTransporte]

    if percentualMoradia < 30 and percentualEducacao < 20 and percentualTransporte < 15:
        resultadoVariavelString = "Seus gastos estão dentro da margem recomendada."
    else: 
        if percentualMoradia > 30:
            controleResultados.append(1)
        else:
            controleResultados.append(0)
        if percentualEducacao > 20:
            controleResultados.append(1)
        else: 
            controleResultados.append(0)
        if percentualTransporte > 15:
            controleResultados.append(1)
        else:
            controleResultados.append(0)

        print("Diagnóstico:")
        for i in range(len(controleResultados)):
            if controleResultados[i] == 1:
                resultadoVariavelString = "Portanto, idealmente, o máximo de sua renda comprometida com {} deveria ser de R$ {}."
                print(resultadoPadraoString.format(nomeDoGasto[i], listaPercentualPorGasto[i], maxPercentualPorGasto[i]))
                print(resultadoVariavelString.format(nomeDoGasto[i], gastoMaxRecomendado[i]))

            elif controleResultados[i] == 0:
                resultadoVariavelString = "Seus gastos estão dentro da margem recomendada."
                print(resultadoPadraoString.format(nomeDoGasto[i], listaPercentualPorGasto[i], maxPercentualPorGasto[i]))
                print(resultadoVariavelString)

#Main
rendaMensal = float(input("Renda mensal total: R$ "))
gastosMoradia = float(input("Gastos totais com moradia: R$ "))
gastosEducacao = float(input("Gastos totais com educação: R$ "))
gastosTransporte = float(input("Gastos totais com transporte: R$ "))

saudeFinanceira(rendaMensal, gastosMoradia, gastosEducacao, gastosTransporte)