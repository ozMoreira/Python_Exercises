import math

print("\n---------------------------------------------------------------------------------------------")
print("    Exemplo de condições booleanas, desenvolvido como exercício da Disciplina de")
print("Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!")

entradaMenu = "1000";
while entradaMenu != "0":
    print("\n---------------------------------------------------------------------------------------------")
    print("\nDigite uma das opções do menu abaixo para acessar o exercicio:")
    print("1 - Número maior que 10?")
    print("2 - Compara números")
    print("3 - Placar de Jogo")
    print("4 - Calculo de Hora Extra")
    print("5 - 'A' é divisível por 'B'?")
    print("6 - Calculo de Raiz Quadrada")
    print("7 - Categoria de Idade")
    print("8 - Calculadora")
    print("9 - Equação do 2º Grau")
    print("10 - \u0394 de Preço x Tipo de Pagamento")
    print("11 - Média Disciplina 'C.T.'")
    print("12 - Valida DATA (Ano não bissexto)")
    print("13 - Valida DATA (Ano bissexto)")
    print("0 - SAIR")
    entradaMenu = input("\nDigite sua opção de menu aqui >>> ")

    #1 - Número maior que 10?
    if (entradaMenu == "1"):
        print("\n---------------------------------------------------------------------------------------------")
        entrada = input("\nInforme um número qualquer para compararmos com 10: >>>> ")    
        if (entrada == 10):
            print("O número informado é exatamente 10")
        elif(entrada > 10):
            print("o número", entrada, "é MAIOR que 10")
        elif (entrada < 10):
            print("O número", entrada, "é MENOR que 10")

    #2 - Compara números
    elif (entradaMenu == "2"):
        print("\n---------------------------------------------------------------------------------------------")
        entrada = int(input("\nInforme um número qualquer inteiro: >>>> "))
        num1 = entrada
        entrada = int(input("\nInforme agora outro número qualquer inteiro: >>>> "))
        num2 = entrada

        if (num1 == num2): 
            print("Opa! Os dois números informados >>>", num1," e ",num2,"<<< são iguais! Temos um empate!")
        elif(num1 > num2):
            print("O primeiro número informado foi >>>", num1, "<<<, e ele é MAIOR que >>>", num2,"<<<")
        elif (num1 < num2):
            print("O segundo número informado >>>", num2,"<<< é Maior que o primeiro número >>>", num1,"<<<")
    
    #3 - Placar de Jogo
    elif (entradaMenu =="3"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nVamos comparar o placar de dois times de futebol!")
        entrada = input("Informe o nome do primeiro time >>> ")
        time1 = entrada
        entrada = input("Informe agora o nome do time adversário>>> ")
        time2 = entrada
        print("\nPerfeito! Então vamos simular agora o jogo:", time1,"x",time2,"!!!")
        print("Informe abaixo quantos gols o", time1,"fez no jogo!!!!")
        entrada = int(input(">>> "))
        golTime1 = entrada
        print("\nAgora, quantos gols o", time2,"fez em seu adversário???")
        entrada = int(input(">>> "))
        golTime2 = entrada

        if (golTime1 > golTime2):
            print("Com o placar de" ,time1,golTime1," x ",golTime2,time2,"...o Grande Campeão foi >>>" ,time1)
        elif (golTime1 < golTime2):
            print("Com o placar de" ,time1,golTime1," x ",golTime2,time2,"...o Grande Campeão foi >>>" ,time2)
        elif (golTime1 == golTime2):
            print("Xiiii, pelo visto a partida não teve um vencedor! Apenas um EMPATE!!!")
    
    #4 - Calculo de Hora Extra
    elif (entradaMenu == "4"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nVamos calcular as horas extras de um colaborador ao final da jornada mensal!")
        entrada = input("Informe a jornada diária (em horas) a ser cumprida (HH:mm) >>> ")
        hora,minuto = entrada.split(':')
        jornadaDiaria = int(hora)+(int(minuto)/60)

        entrada = float(input("Qual o valor do salario mensal do colaborador? >>> R$ "))
        salarioMensal = entrada

        entrada = int(input("Informe o total de dias úteis do mês trabalhado >>> "))
        totalDiasUteis = entrada

        entrada = input("Informe o total de horas trabalhadas no mês (HHH:00)>>> ")
        hora,minuto = entrada.split(':')
        totalHorasTrabalhadas = int(hora)+(int(minuto)/60)
        salarioHora = float((salarioMensal / totalDiasUteis)/jornadaDiaria)
        totalHorasRegular = totalDiasUteis * jornadaDiaria
        horaExtra = float(totalHorasTrabalhadas - totalHorasRegular)
        print("\nValor do Salario:  R$ {:.2f}".format(salarioMensal)," equivale a R$ {:.2f}".format(salarioHora),"/ hora")
  
        if (horaExtra == 0):
            print("\n\nColaborador não tem horas extras pra receber, pois cumpriu sua jornada exata de {:.2f}".format(totalHorasRegular)," horas mensais")
        elif (horaExtra > 0):
            valorTotalHE = float(horaExtra * (salarioHora + (salarioHora*50)/100))
            salarioExtra = float(salarioMensal + valorTotalHE)
            print("\n\nColaborador te {:.2f}" .format(horaExtra), "horas extras pra receber, no valor de R$ {:.2f}" .format(valorTotalHE)," e seu salário\nneste mês será de  R$ {:.2f}".format(salarioExtra))
    
    #5 - 'A' é divisível por 'B'?
    elif (entradaMenu == "5"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nVamos calcular agora a divisibilidade de dois números, ou seja, se seu resto é '0'")
        entrada = int(input("\nInforme o primeiro número inteiro qualquer >>> "))
        numA = entrada
        entrada = int(input("Informe o segundo número inteiro qualquer >>> "))
        numB = entrada
        resultado = numA % numB
        
        if (resultado == 0):
            print("\n\nO número", numA,"é perfeitamente divisível por", numB)
        else:
            print("\n\n",numA,"NÃO é divisível por", numB,"pois seu resto é", resultado)
    
    #6 - Calculo de Raiz Quadrada
    elif (entradaMenu == "6"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nCalcularemos agora a RAIZ QUADRADA de um número, lembre-se que se vc digitar um número negativo\no sistema solicitará um número positivo válido para o calculo:")
        entrada = float(input("\nInforme um número que deseja saber sua Raiz Quadrada >>> "))
        numA = entrada

        while numA < 0:
            print("\nO número",numA,"é negativo, e por isso não é possível cacular sua raiz quadrada!")
            entrada = float(input("Informe um numero positivo para o calculo >>>"))
            numA = entrada            
        if (numA >= 0): 
            resultado = math.sqrt(numA)
            print("\nA Raiz Quadrada de",numA, "é {:.1f}".format(resultado))
    
    #7 - Categoria de Idade
    elif (entradaMenu == "7"):
        print("\n---------------------------------------------------------------------------------------------")
        entrada = float(input("\nInforme sua idade para calcularmos o seu nivel de senioridade na Natação: >>> "))
        idade = entrada

        if idade < 5:
            print("\nA idade mínima para a primeira categoria é de 5 anos! Ainda terá que esperar um pouco\npra poder competir!")
        elif idade >= 5 and idade <= 7:
            print("\nSua categoria é >>> Infantil <<<")  
        elif idade >= 8 and idade <= 10:
            print("\nSua categoria é >>> Juvenil <<<")  
        elif idade >= 11 and idade <= 15:
            print("\nSua categoria é >>> Adolescente <<<")
        elif idade >= 16 and idade <= 30:
            print("\nSua categoria é >>> Adulto <<<")
        else:
            print("\nSua categoria é >>> Senior <<<")

    #8 - Calculadora
    elif (entradaMenu == "8"):
        print("\n---------------------------------------------------------------------------------------------")
        entrada = float(input("\nInforme o primeiro numero que deseja utilizar no calculo: >>> "))
        numA = entrada
        entrada = float(input("Informe o segundo numero que deseja utilizar no calculo: >>> "))
        numB = entrada
        entrada = input("Informe a operação desejada (+  -  /  *): >>> ")
        op = entrada

        if op == "+":
            resultado = float(numA + numB)
            print("\nO resultado de   " ,numA,"+",numB,"   é   " ,resultado)
        elif op == "-":
            resultado = float(numA - numB)
            print("\nO resultado de   " ,numA,"-",numB,"   é   " ,resultado)
        elif op == "/":
            if numB == 0:
                print("\nNão é possível dividir nenhum número por 0")
            else:
                resultado = float(numA / numB)
                print("\nO resultado de   " ,numA,"/",numB,"   é   " ,resultado)
        elif op == "*":
            resultado = float(numA * numB)  
            print("\nO resultado de   " ,numA,"*",numB,"   é   " ,resultado)
        else:
            print("\nVoce digitou uma opção de Operação Aritmética inválida")

    #9 - Equação do 2º Grau
    elif (entradaMenu == "9"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nUma equação é uma igualdade com uma ou mais incógnitas. Vamos calcular o valor de \u0394 e\nsuas raizes reais")
        entrada = int(input("\nInforme um valor inteiro não nulo para a incognita 'a' >>> "))
        numA = entrada
        entrada = int(input("Informe um valor inteiro para a incognita 'b' >>> "))
        numB = entrada
        entrada = int(input("Informe um valor inteiro para a incognita 'c' >>> "))
        numC = entrada

        while (numA == 0):
            print("\n>>>>>> Por gentileza, escolha outro número diferente de '0' para a incognita 'a' <<<<< ")
            entrada = int(input("\nInforme um valor inteiro não nulo para a incognita 'a' >>> "))
            numA = entrada
            entrada = int(input("Informe um valor inteiro para a incognita 'b' >>> "))
            numB = entrada
            entrada = int(input("Informe um valor inteiro para a incognita 'c' >>> "))
            numC = entrada

        if (numA != 0): 
            delta = (numB * numB) - 4 * numA * numC
            raizDelta = delta ** 0.5
            raiz1 = ((numB * -1) + raizDelta)/(2*numA)
            raiz2 = ((numB * -1) - raizDelta)/(2*numA)

            print("\nO valor de \u0394 para os valores informados, é >>> ", delta)
            print("A Raiz de x' é >>> {:.2f}".format(raiz1),"e a raiz de x'' é {:.2f}>>> ".format(raiz2))
   
    #10 - Variação de Preço x Tipo de Pagamento
    elif (entradaMenu == "10"):   
        print("\n---------------------------------------------------------------------------------------------")
        print("\nVamos agora simular a alteração de um preço de etiqueta, de acordo com a forma de pagamento!")
        entrada = float(input("\nInforme o valor de um produto, conforme 'consta' na etiqueta >>> R$ "))
        precoLabel = entrada
        print("\nInforme agora a forma de pagamento, de acordo com as opções abaixo!")
        print("\n-------------------------------------------------------------------------")
        print("|              Cheque à Vista - 10% off- (Digite 'C')                   |")
        print("|         Cartão de Credito à Vista - 5% off - (Digite 'CC')            |")                   
        print("|             Parcelado em 2 sem juros - (Digite 'P2')                  |")
        print("|     Parcelado 4 vezes - Juros de 7% no valor total - (Digite 'P4')    |")
        print("-------------------------------------------------------------------------")
        entrada = input("\nInforme a opção de pagamento desejada >>> ").upper()
        tp_pagamento = entrada
   
        while (tp_pagamento != "C" and tp_pagamento != "CC" and tp_pagamento != "P2" and tp_pagamento != "P4"):
            print("\nATENÇÃO!!!!!!!!! Método de pagamento INVALIDO!")
            print("\n-------------------------------------------------------------------------")
            print("|              Cheque à Vista - 10% off- (Digite 'C')                   |")
            print("|         Cartão de Credito à Vista - 5% off - (Digite 'CC')            |")                   
            print("|             Parcelado em 2 sem juros - (Digite 'P2')                  |")
            print("|     Parcelado 4 vezes - Juros de 7% no valor total - (Digite 'P4')    |")
            print("-------------------------------------------------------------------------")
            entrada = input("\nInforme a opção de pagamento desejada para o produto informado >>>> ").upper()
            tp_pagamento = entrada

        if (tp_pagamento == "C"):
            precoAplicado = precoLabel - ((precoLabel * 10) / 100)
            print("\nPara pagamento no Cheque a Vista, o valor do produto será >>>  R${:.2f} ".format(precoAplicado)," <<<")
        elif (tp_pagamento == "CC"):
            precoAplicado = precoLabel - ((precoLabel * 5) / 100)
            print("\nPara pagamento no Cartão de Crédito a Vista, o valor do produto será >>>  R${:.2f} ".format(precoAplicado)," <<<")
        elif (tp_pagamento == "P2"):
            precoAplicado = precoLabel/2
            print("\nPara pagamento Parcelado em 2x, o valor do produto continua sendo >>>  R${:.2f} ".format(precoLabel)," <<<\ne o valor de cada parcela será de  >>>  R${:.2f} ".format(precoAplicado)," <<<")
        elif (tp_pagamento == "P4"):
            precoJuros = precoLabel + ((precoLabel * 7) / 100)
            precoAplicado = precoJuros/2
            print("\nPara pagamento Parcelado em 4x, o valor do produto será >>>  R${:.2f} ".format(precoJuros)," <<<\ne o valor de cada parcela será de  >>>  R${:.2f} ".format(precoAplicado)," <<<")              
    
    #11 - Média Disciplina 'C.T.'
    elif(entradaMenu == "11"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nCalculo de Média e Verificação de Aprovaão ou Reprovação Semestral!")
        print("Disciplina de Computational Thinking - FIAP 2021!")
        entrada = input("\n Informe o nome do Aluno >>> ")
        aluno = entrada
        entrada = float(input(" Informe a média do Primeiro Semestre >>> "))
        sem1 = entrada
        entrada = float(input(" Informe a média do Segundo Semestre  >>> "))
        sem2 = entrada
        entrada = float(input(" Quantas aulas o aluno assistiu no total?  >>> "))
        aulasAluno = entrada
        entrada = float(input(" Quantas aulas foram apresentadas no total??  >>> "))
        aulasProf = entrada
     
        sem1Peso = sem1 * 4
        sem2Peso = sem2 * 6
        mediaFinal = (sem1Peso + sem2Peso)/10
        percentEvasaoAluno = ((aulasProf-aulasAluno)/aulasAluno)*100
        nFaltas = aulasProf - aulasAluno
        presencaValidada = 100 - percentEvasaoAluno
        
        if (mediaFinal > 6 and presencaValidada > 70):
            print("\n\nParabéns! O aluno", aluno,"foi APROVADO com média final {:.2f}" .format(mediaFinal), "e participou de {:.2f}" .format(presencaValidada),"% das aulas")
        elif (mediaFinal >= 4 and mediaFinal <= 5.9 and presencaValidada > 70):
            print("\n\nO aluno", aluno,"terá que ficar de EXAME, pois está com Média Final {:.2f}" .format(mediaFinal), " mesmo participando de {:.2f}" .format(presencaValidada),"% das aulas")
        elif (mediaFinal < 4 and presencaValidada > 70):
            print("\n\nO aluno", aluno,"foi REPROVADO, pois está com Média Final {:.2f}" .format(mediaFinal), " mesmo participando de {:.2f}" .format(presencaValidada),"% das aulas")
        elif ( mediaFinal > 4 and presencaValidada < 70 ):
            print("\n\nO aluno", aluno,"está REPROVADO por falta, pois compareceu apenas a {:.2f}" .format(presencaValidada),"% do total de", aulasProf, "aulas, independente de sua Média Final que foi {:.2f}".format(mediaFinal))
    
    #12 - Valida DATA (Ano não bissexto)
    elif(entradaMenu == "12"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nValidação de uma data qualquer (DD e MM) de um ano não bissexto")
        entrada = int(input("\n Informe um dia qualquer (DD) >>> "))
        dia = entrada
        entrada = input(" Informe um mês qualquer (mm) >>> ")
        mes = entrada

        if (dia >= 1 and dia <=31 and mes == "01"):
            print("\nO dia", dia, "é válido para o mês de Janeiro")
        elif (dia >= 1 and dia <=28 and mes == "02"):
            print("\nO dia", dia, "é válido para o mês de Fevereiro")
        elif (dia >= 1 and dia <=31 and mes == "03"):
            print("\nO dia", dia, "é válido para o mês de Março")
        elif (dia >= 1 and dia <=30 and mes == "04"):
            print("\nO dia", dia, "é válido para o mês de Abril")
        elif (dia >= 1 and dia <=31 and mes == "05"):
            print("\nO dia", dia, "é válido para o mês de Maio")
        elif (dia >= 1 and dia <=30 and mes == "06"):
            print("\nO dia", dia, "é válido para o mês de Junho")    
        elif (dia >= 1 and dia <=31 and mes == "07"):
            print("\nO dia", dia, "é válido para o mês de Julho")
        elif (dia >= 1 and dia <=31 and mes == "08"):
            print("\nO dia", dia, "é válido para o mês de Agosto") 
        elif (dia >= 1 and dia <=30 and mes == "09"):
            print("\nO dia", dia, "é válido para o mês de Setembro")    
        elif (dia >= 1 and dia <=31 and mes == "10"):
            print("\nO dia", dia, "é válido para o mês de Outubro")    
        elif (dia >= 1 and dia <=30 and mes == "11"):
            print("\nO dia", dia, "é válido para o mês de Novembro")    
        elif (dia >= 1 and dia <=31 and mes == "12"):
            print("\nO dia", dia, "é válido para o mês de Dezembro")
        else:
            print("\n::::ATENÇÃO:::: A data informada não é válida")

    #13 - Valida DATA (Ano bissexto)
    elif(entradaMenu == "13"):
        print("\n---------------------------------------------------------------------------------------------")
        print("\nValidação de ano bissexto para prosseguir se uma data é correta")
        entrada = int(input("\n Informe um dia qualquer (DD) >>> "))
        dia = entrada
        entrada = input(" Informe um mês qualquer (mm) >>> ")
        mes = entrada
        entrada = int(input(" Informe um ano (aaaa) >>> "))
        ano = entrada

        validaAno1 = (ano%4)
        validaAno2 = (ano%100)
        validaAno3 = (ano%400)


        #se ele for divisivel por 4 e não for multiplo de 100
        if (validaAno1 == 0 and validaAno2 !=0):
            print("Ano é bissexto")
            if (dia >= 1 and dia <=31 and mes == "01"):
                print("\nO dia", dia, "é válido para o mês de Janeiro")
            elif (dia >= 1 and dia <=29 and mes == "02"):
                print("\nO dia", dia, "é válido para o mês de Fevereiro")
            elif (dia >= 1 and dia <=31 and mes == "03"):
                print("\nO dia", dia, "é válido para o mês de Março")
            elif (dia >= 1 and dia <=30 and mes == "04"):
                print("\nO dia", dia, "é válido para o mês de Abril")
            elif (dia >= 1 and dia <=31 and mes == "05"):
                print("\nO dia", dia, "é válido para o mês de Maio")
            elif (dia >= 1 and dia <=30 and mes == "06"):
                print("\nO dia", dia, "é válido para o mês de Junho")    
            elif (dia >= 1 and dia <=31 and mes == "07"):
                print("\nO dia", dia, "é válido para o mês de Julho")
            elif (dia >= 1 and dia <=31 and mes == "08"):
                print("\nO dia", dia, "é válido para o mês de Agosto") 
            elif (dia >= 1 and dia <=30 and mes == "09"):
                print("\nO dia", dia, "é válido para o mês de Setembro")    
            elif (dia >= 1 and dia <=31 and mes == "10"):
                print("\nO dia", dia, "é válido para o mês de Outubro")    
            elif (dia >= 1 and dia <=30 and mes == "11"):
                print("\nO dia", dia, "é válido para o mês de Novembro")    
            elif (dia >= 1 and dia <=31 and mes == "12"):
                print("\nO dia", dia, "é válido para o mês de Dezembro")
            else:
                print("\n::::ATENÇÃO:::: A data informada não é válida")
        #se ele não for divisivel por 4 mas for divisível por 400
        elif(validaAno1 != 0 and validaAno3 == 0):
            if (dia >= 1 and dia <=31 and mes == "01"):
                print("\nO dia", dia, "é válido para o mês de Janeiro")
            elif (dia >= 1 and dia <=29 and mes == "02"):
                print("\nO dia", dia, "é válido para o mês de Fevereiro")
            elif (dia >= 1 and dia <=31 and mes == "03"):
                print("\nO dia", dia, "é válido para o mês de Março")
            elif (dia >= 1 and dia <=30 and mes == "04"):
                print("\nO dia", dia, "é válido para o mês de Abril")
            elif (dia >= 1 and dia <=31 and mes == "05"):
                print("\nO dia", dia, "é válido para o mês de Maio")
            elif (dia >= 1 and dia <=30 and mes == "06"):
                print("\nO dia", dia, "é válido para o mês de Junho")    
            elif (dia >= 1 and dia <=31 and mes == "07"):
                print("\nO dia", dia, "é válido para o mês de Julho")
            elif (dia >= 1 and dia <=31 and mes == "08"):
                print("\nO dia", dia, "é válido para o mês de Agosto") 
            elif (dia >= 1 and dia <=30 and mes == "09"):
                print("\nO dia", dia, "é válido para o mês de Setembro")    
            elif (dia >= 1 and dia <=31 and mes == "10"):
                print("\nO dia", dia, "é válido para o mês de Outubro")    
            elif (dia >= 1 and dia <=30 and mes == "11"):
                print("\nO dia", dia, "é válido para o mês de Novembro")    
            elif (dia >= 1 and dia <=31 and mes == "12"):
                print("\nO dia", dia, "é válido para o mês de Dezembro")
            else:
                print("\n::::ATENÇÃO:::: A data informada não é válida")
        #se ele for multiplo de 100 mas for divisivel por 400 tb
        elif(validaAno2 == 0 and validaAno3 == 0):
            if (dia >= 1 and dia <=31 and mes == "01"):
                print("\nO dia", dia, "é válido para o mês de Janeiro")
            elif (dia >= 1 and dia <=29 and mes == "02"):
                print("\nO dia", dia, "é válido para o mês de Fevereiro")
            elif (dia >= 1 and dia <=31 and mes == "03"):
                print("\nO dia", dia, "é válido para o mês de Março")
            elif (dia >= 1 and dia <=30 and mes == "04"):
                print("\nO dia", dia, "é válido para o mês de Abril")
            elif (dia >= 1 and dia <=31 and mes == "05"):
                print("\nO dia", dia, "é válido para o mês de Maio")
            elif (dia >= 1 and dia <=30 and mes == "06"):
                print("\nO dia", dia, "é válido para o mês de Junho")    
            elif (dia >= 1 and dia <=31 and mes == "07"):
                print("\nO dia", dia, "é válido para o mês de Julho")
            elif (dia >= 1 and dia <=31 and mes == "08"):
                print("\nO dia", dia, "é válido para o mês de Agosto") 
            elif (dia >= 1 and dia <=30 and mes == "09"):
                print("\nO dia", dia, "é válido para o mês de Setembro")    
            elif (dia >= 1 and dia <=31 and mes == "10"):
                print("\nO dia", dia, "é válido para o mês de Outubro")    
            elif (dia >= 1 and dia <=30 and mes == "11"):
                print("\nO dia", dia, "é válido para o mês de Novembro")    
            elif (dia >= 1 and dia <=31 and mes == "12"):
                print("\nO dia", dia, "é válido para o mês de Dezembro")
            else:
                print("\n::::ATENÇÃO:::: A data informada não é válida")
        #se não for bissexto, fevereiro terá 28 dias
        else:
            if (dia >= 1 and dia <=31 and mes == "01"):
                print("\nO dia", dia, "é válido para o mês de Janeiro")
            elif (dia >= 1 and dia <=28 and mes == "02"):
                print("\nO dia", dia, "é válido para o mês de Fevereiro")
            elif (dia >= 1 and dia <=31 and mes == "03"):
                print("\nO dia", dia, "é válido para o mês de Março")
            elif (dia >= 1 and dia <=30 and mes == "04"):
                print("\nO dia", dia, "é válido para o mês de Abril")
            elif (dia >= 1 and dia <=31 and mes == "05"):
                print("\nO dia", dia, "é válido para o mês de Maio")
            elif (dia >= 1 and dia <=30 and mes == "06"):
                print("\nO dia", dia, "é válido para o mês de Junho")    
            elif (dia >= 1 and dia <=31 and mes == "07"):
                print("\nO dia", dia, "é válido para o mês de Julho")
            elif (dia >= 1 and dia <=31 and mes == "08"):
                print("\nO dia", dia, "é válido para o mês de Agosto") 
            elif (dia >= 1 and dia <=30 and mes == "09"):
                print("\nO dia", dia, "é válido para o mês de Setembro")    
            elif (dia >= 1 and dia <=31 and mes == "10"):
                print("\nO dia", dia, "é válido para o mês de Outubro")    
            elif (dia >= 1 and dia <=30 and mes == "11"):
                print("\nO dia", dia, "é válido para o mês de Novembro")    
            elif (dia >= 1 and dia <=31 and mes == "12"):
                print("\nO dia", dia, "é válido para o mês de Dezembro")
            else:
                print("\n::::ATENÇÃO:::: A data informada não é válida")
    else:
        print("\n---------------------------------------------------------------------------------------------")
        print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::\n      Opção Escolhida Inválida! Selecione uma das opções no Menu abaixo!")
print("---------------------------------------------------------------------------------------------")