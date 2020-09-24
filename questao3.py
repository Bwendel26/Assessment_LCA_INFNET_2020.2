# -*- coding: utf-8 -*-

# "Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, 
# no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. 
# Esses valores não devem ser totalmente desprezados, mas não podem funcionar como 
# um norte para o orçamento doméstico de todas as famílias." Fonte: BTG Pactual Digital.

# Crie um programa contendo uma função que, dados um valor de renda mensal total,
# gastos totais com moradia, gastos totais com educação e gastos totais com transporte, 
# faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais 
# acima expostos, informando qual é o percentual da renda mensal total comprometido 
# por cada custo. 

# Se o gasto estiver dentro do percentual recomendado, informe ainda que 

# Seus gastos estão dentro da margem recomendada.

# Caso contrário, informe:

# Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
  
# Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor 
# equivalente ao percentual máximo de gasto com esse tipo de custo.

# Exemplo de saída do programa:

# Renda mensal total: R$ 5000
# Gastos totais com moradia: R$ 1760
# Gastos totais com educação: R$ 800
# Gastos totais com transporte: R$ 300

# Diagnóstico:
# Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 30%. 
# Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ 1500.
# Seus gastos totais com educação comprometem 16% de sua renda total. O máximo recomendado é de 20%. 
# Seus gastos estão dentro da margem recomendada.
# Seus gastos totais com transporte comprometem 6% de sua renda total. O máximo recomendado é de 15%. 
# Seus gastos estão dentro da margem recomendada.


def saudeFinanceira(rendaMensal, gastosMoradia, gastosEducacao, gastosTransporte):
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