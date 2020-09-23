Este é o Assessment da disciplina Lógica, Computação e Algoritmos. Este assessment está organizado em projetos, para que você possa demonstrar as competências trabalhadas nas etapas 1 a 9 da disciplina. 

Questão 1

O Pensamento Computacional se destaca como uma das mais importantes novas competências do século XXI. Ele foi o tema central da primeira fase dos nossos estudos na disciplina. 

    Realize uma captura de tela com todo o seu progresso do curso acelerado do code.org, demonstrando a conclusão de todas as etapas do curso. Anexe, ainda, o certificado de conclusão gerado. 
    Explique, com suas palavras, cada um dos quatro vetores do Pensamento Computacional: Abstração, Decomposição, Reconhecimento de Padrões e Algoritmos. Use exemplos para apoiar sua argumentação.

Questão 2

Pesquise pelas linguagens de programação, tecnologias, como banco de dados e outras usadas por empresas de aplicações conhecidas do nosso cotidiano.

    Conceitualize back-end e front-end de uma aplicação e aponte as principais diferenças. Use exemplos de aplicações do dia a dia e até mesmo capturas de tela e imagens para ilustrar sua resposta.
    Conceitualize banco de dados e cite exemplos de como eles podem contribuir nas aplicações que usamos no dia a dia. Novamente, cabem analogias com aplicações usadas no cotidiano.

Questão 3 

Considere o argumento abaixo:

    Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. Esses valores não devem ser totalmente desprezados, mas não podem funcionar como um norte para o orçamento doméstico de todas as famílias.

Fonte: BTG Pactual Digital

Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. 

Se o gasto estiver dentro do percentual recomendado, informe ainda que 

Seus gastos estão dentro da margem recomendada.

Caso contrário, informe:


Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
  

Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

Exemplo de saída do programa:


Renda mensal total: R$ 5000
Gastos totais com moradia: R$ 1760
Gastos totais com educação: R$ 800
Gastos totais com transporte: R$ 300

Diagnóstico:
Seus gastos totais com moradia comprometem 35.2% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ 1500.
Seus gastos totais com educação comprometem 16% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.
Seus gastos totais com transporte comprometem 6% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.
  

Questão 4

Seja a seguinte citação:

    Osjuros compostos são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma confiável e sistemática acumulação de riqueza

A frase, curiosamente, é de Albert Einstein, não de algum banqueiro ou gestor de fundos de capitais. 

Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.

No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.

No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.

Ao final de 120 meses, você terá o montante final de R$187.303,05.

    Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

    Exemplo de saída do programa:


    Valor inicial: R$ 10000
    Rendimento por período (%): 0.54
    Aporte a cada período: R$ 1000
    Total de períodos: 120 

    Após 1 períodos(s), o montante será de R$11054.00.
    Após 2 períodos(s), o montante será de R$12113.69.
    Após 3 períodos(s), o montante será de R$13179.11.
    Após 4 períodos(s), o montante será de R$14250.27.
    Após 5 períodos(s), o montante será de R$15327.22.
    (...)
    Após 115 períodos(s), o montante será de R$177406.76.
    Após 116 períodos(s), o montante será de R$179364.76.
    Após 117 períodos(s), o montante será de R$181333.33.
    Após 118 períodos(s), o montante será de R$183312.53.
    Após 119 períodos(s), o montante será de R$185302.42.
    Após 120 períodos(s), o montante será de R$187303.05.
      



    Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.

Questão 5

Considere a seguinte projeção de PIBs feita pelo FMI em 2014:

Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020 – ordem decrescente de 2014)*

País
	

2013
	

2014
	

2015
	

2016
	

2017
	

2018
	

2019
	

2020

EUA
	

16.76
	

17.41
	

18.12
	

18.95
	

19.86
	

20.76
	

21.61
	

22.48

China
	

9.46
	

10.38
	

11.21
	

11.96
	

12.86
	

13.87
	

14.96
	

16.15

Japão
	

4.92
	

4.61
	

4.21
	

4.34
	

4.48
	

4.59
	

4.75
	

4.93

Alemanha
	

3.73
	

3.86
	

3.41
	

3.51
	

3.64
	

3.78
	

3.93
	

4.1

Reino Unido
	

2.68
	

2.94
	

2.85
	

2.98
	

3.14
	

3.32
	

3.51
	

3.73

França
	

2.8
	

2.84
	

2.47
	

2.52
	

2.62
	

2.73
	

2.86
	

3.01

Brasil
	

2.39
	

2.35
	

1.9
	

1.92
	

2.03
	

2.13
	

2.24
	

2.35

Itália
	

2.13
	

2.14
	

1.84
	

1.88
	

1.94
	

2.01
	

2.08
	

2.17

Índia
	

1.87
	

2.05
	

2.3
	

2.51
	

2.75
	

3.01
	

3.31
	

3.64

Rússia
	

2.07
	

2.05
	

1.17
	

1.37
	

1.52
	

1.69
	

1.88
	

2.08

Canadá
	

1.83
	

1.78
	

1.61
	

1.68
	

1.76
	

1.85
	

1.94
	

2.04

Coreia do Sul
	

1.3
	

1.41
	

1.43
	

1.51
	

1.61
	

1.73
	

1.86
	

2.01

Espanha
	

1.39
	

1.4
	

1.23
	

1.26
	

1.3
	

1.35
	

1.41
	

1.48

México
	

1.26
	

1.28
	

1.23
	

1.3
	

1.37
	

1.46
	

1.55
	

1.65

Indonésia
	

9.13
	

8.89
	

8.96
	

9.52
	

1.03
	

1.11
	

1.2
	

1.3

*Dados de 2014; dados de 2015 em diante eram previsões do FMI em 2014. Fonte.

Faça download dos dados em: 

Lista_Revisão_PIBs

(Use a função Arquivo → Fazer o download → csv, para baixar uma versão formatada dos dados para usá-los no projeto)

    Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano. 
        O programa solicita ao usuário o nome do país e o ano desejado.
        Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 

        País não disponível.

        ou

        Ano não disponível.

        a depender do tipo de dado não encontrado. 

        Exemplo de saída do programa:


        Informe um país: Brasil
        Informe um ano entre 2013 e 2020: 2020
        PIB Brasil em 2020: US$2.35 trilhões.
          

    Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.

    Exemplo de saída do programa:


    EUA                  Variação de 34.13% entre 2013 e 2020.
    China                Variação de 70.72% entre 2013 e 2020.
    Japão                Variação de 0.2% entre 2013 e 2020.
    Alemanha             Variação de 9.92% entre 2013 e 2020.
    Reino Unido          Variação de 39.18% entre 2013 e 2020.
    França               Variação de 7.5% entre 2013 e 2020.
    Brasil               Variação de -1.67% entre 2013 e 2020.
    Itália               Variação de 1.88% entre 2013 e 2020.
    Índia                Variação de 94.65% entre 2013 e 2020.
    Rússia               Variação de 0.48% entre 2013 e 2020.
    Canadá               Variação de 11.48% entre 2013 e 2020.
    Coreia do Sul        Variação de 54.62% entre 2013 e 2020.
    Espanha              Variação de 6.47% entre 2013 e 2020.
    México               Variação de 30.95% entre 2013 e 2020.
    Indonésia            Variação de -85.76% entre 2013 e 2020.
      

    Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.

        A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
        O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
