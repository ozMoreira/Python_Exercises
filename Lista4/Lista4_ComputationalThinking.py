import random

entradaMenu = "999"
while entradaMenu != "0":
    print("\n---------------------------------------------------------------------------------------------")
    print("         Seja bem vindo à LISTA DE EXERCÍCIOS 4 de COMPUTATIONAL THINKING USING PYTHON")
    print("---------------------------------------------------------------------------------------------")
    print("\nDigite uma das opções do menu abaixo para acessar o exercicio:")
    print("1 - Soma Pares da Sequencia")
    print("2 - Media da Sala")
    print("3 - Calcula Aprovados e Reprovados")
    print("4 - Conta Positivos e Negativos")
    print("5 - Contagem dos divisores positivos de N    ")
    print("6 - Calculo de Notas do Concurso")
    print("7 - Tabela de Temp. (F to C)")
    print("8 - Verifica se é Número Primo")
    print("9 - Calcula Juros Mensal")
    print("10 - Calculo Fatorial")
    print("11 - Sequencia de Fibonacci")
    print("12 - Verifica se é Palíndrome")
    print("13 - Jogo da Advinhacao")
    print("14 - Numeros Perfeitos")
    print("15 - Segmento Crescente")
    print("16 - Calculo de Digito com Método de Módulo 10")
    print("17 - Raiz Quadrada (exata e não exata")
    print("0 - SAIR")
    entradaMenu = input("\nDigite sua opção de menu aqui >>> ")
   
#Ex. 1 - Lista 4 - Soma pares da sequencia
#    Dada uma sequência de números inteiros onde o último elemento é o 0,
#    escreva um algoritmo que calcula a soma dos números pares da sequência.
    if entradaMenu == "1":
        print("\n---------------------------------------------------------------------------------------------"
             +"\nEx. 1 - Lista 4 - Soma pares da sequencia"
             +"\nSerá pedido uma sequencia qualquer de números ao usuario, e só deve parar de pedir ao digitar 0"
             +"\napos a sequencia ser informada, o sistema deverá calcular a soma dos números pares apenas."
             +"\n\n---------------------------------------------------------------------------------------------")

        numInformado = str(input("\nInforme um número qualquer >>> "))
        soma = 0
        seq = ""
        while numInformado != "0":
            seq += str(numInformado + ", ")
            num = int(numInformado)
            checkPar = num%2
            numInformado = str(input("Informe um número qualquer >>> "))
            if checkPar == 0:
                soma +=num
        print("A a soma dos números pares da sequencia '",seq, "' resulta em: ", soma)

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      
    
#Ex. 2 Lista 4 - Media da classe
#    Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova,
#    determinar a média das notas dessa turma. Considere que o usuário digite as informações corretamente.
    if entradaMenu == "2":
        print("\n---------------------------------------------------------------------------------------------"
             +"\nEx. 2 - Lista 4 - Média da Turma"
             +"\nUsuario informa um numero 'x' de Alunos bem como suas notas sequencialmente. O Algorítmo"
             +"\ncalcula a média das notas da turma."
             +"\n\n---------------------------------------------------------------------------------------------")

        aux = input("\nInforme um número qualquer de alunos >>> ")
        nroAlunos = int(aux)
        i = 1
        soma = 0
        print("")
        while i <= nroAlunos:
            aux = input("Informe sequencialmente, a nota dos alunos >>>")
            nota = float(aux)
            soma += nota
            i += 1
        media = soma/nroAlunos
        print("\nA média da classe foi {:.2f}" .format(media))

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      
    
#Ex. 3 Lista 4 - Media da classe
#   Informa a média da turma, e conta alunos que tiraram média entre 0 e 5 e os que tiraram acima de 5.
    if entradaMenu == "3":
        print("\n---------------------------------------------------------------------------------------------"
             +"\nEx. 3 - Lista 4 -Conta alunos com nota abaixo de 5 e notas igual ou superior a 5"
             +"\nImplementa no algoritmo anterior, uma contagem de alunos que tiraram nota acima ou igual a 5"
             +"\ne alunos com nota abaixo de 5"
             +"\n\n---------------------------------------------------------------------------------------------")

        aux = input("\nInforme um número qualquer de alunos >>> ")
        nroAlunos = int(aux)
        i = 1
        soma = 0
        contaReprovado = 0
        contaAprovado = 0
        print("")
        while i <= nroAlunos:
            aux = input("Informe sequencialmente, a nota dos alunos >>>")
            nota = float(aux)
            soma += nota
            i += 1
            if nota >= 0 and nota < 5:
                contaReprovado += 1
            else:
                contaAprovado += 1
        media = soma/nroAlunos
        print("\nA média da classe foi {:.2f}" .format(media))
        print("No total,>>>",contaReprovado, "<<< alunos tiraram nota entre 0 e 5 e >>>", contaAprovado, "<<< tiraram nota 5 ou superior.")
        
        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 4 Lista 4 - Conta Números Positivos e Negativos
#   Dados n um inteiro positivo e uma sequência de n números reais, escreva um algoritmo que
#   conta e imprime a quantidade de números positivos e a quantidade de números negativos.
    if entradaMenu == "4":
        print("\n---------------------------------------------------------------------------------------------"
             +"\nEx. 4 - Lista 4 - Conta números positivos e negativos"
             +"\nO sistema pede ao usuario um número que sera usado como 'senha', para saber quando deverá parar"
             +"\nde pedir novos números. Enquanto a senha nao for informada o algoritmo pede um número e ao final"
             +"\nconta a quantidade de números, segregando os positivos dos negativos."
             +"\n\n---------------------------------------------------------------------------------------------")

        aux = input("Informe um número 'senha' que sera utilizado para identificar quando voce nao quiser mais"
                    +"\ncontinuar informando números ao computador: >>> ")
        n = int(aux)
        positivos = 0
        negativos = 0
        contaN = 0
        
        while contaN < n:
            numReal = float(input("Informe um número real (Positivo ou Negativo) >>> "))
            if numReal > 0:
                positivos += 1   
                
            if numReal <= 0:
                negativos += 1 
            contaN = contaN + 1                                         
        print("Voce informou ", positivos, "números positivos e ", negativos, "negativos!")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      
       
#Ex. 5 Lista 4 - Conta Divisores de N
#   Escreva um algoritmo que, dados um número inteiro positivo n, imprime na tela a contagem de todos os divisores positivos de n.
    if entradaMenu == "5":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 5 - Lista 4 - Conta divisores de N"
        +"\nO sistema pede ao usuario um numero qualquer, em seguida o algoritmo calcula sua divisão e conta"
        +"\no numero total de divisores inteiros"
        +"\n---------------------------------------------------------------------------------------------")

        num = int(input("\n\nInsira um número para contagem dos seus divisores >>> "))
        div = 1
        contDivisores = 0
        while div <= num:
            resto = num % div
            div = div +1
            if resto == 0:
                contDivisores +=1
        print("\nO número", num, "pode ser dividido por um total de", contDivisores,"divisores")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      
            
#Ex. 6 Lista 4 - Calculo de notas de um concurso
#Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo. Sabendo que
#cada questão vale 1 ponto, escreva um algoritmo que lê a pontuação da prova obtida de cada
#um dos candidatos e calcula:
#a) a maior e a menor nota
#b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram
#de 21 a 50 e o percentual que acertou acima de 50 questões
    if entradaMenu == "6":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 6 - Lista 4 - Calculo de Notas do Concurso"
        +"\nEste algoritmo calcula as maiores e menores notas em tempo real, logo apos o Input, calculando"
        +"\ntambém os percentuais de acerto distribuidos por 3 grupos: Quem acerto ate 20 questões, entre"
        +"\n21 e 50 e acima de 50, apresentando os dados em percentuais sobre o total de candidadtos"
        +"\n---------------------------------------------------------------------------------------------")

        totalCandidatos = 1
        maiorNota = 0
        menorNota = 70
        conta1 = 0
        conta2 = 0
        conta3 = 0
        while totalCandidatos <= 20:
            notaInformada = int(input("Informe a próxima Nota do concurso >>> "))
            if notaInformada > 50:
                conta3 += 1
            elif notaInformada > 20 and notaInformada < 51:
                conta2 += 1
            else:
                conta1 += 1
            totalCandidatos += 1
            if notaInformada > maiorNota:
                maiorNota = notaInformada
                print("Maior pontuação até o momento")
            elif notaInformada < menorNota:
                menorNota = notaInformada
                print("Menor pontuação até o momento")
        media1 = (conta1 * 100) / 20
        media2 = (conta2 * 100) / 20
        media3 = (conta3 * 100) / 20
        print (media1, "% dos candidatos tiraram 20 pontos ou menos.")
        print (media2, "% dos candidatos tiraram entre 21 e 50 pontos.")
        print (media3, "% dos candidatos acertaram mais de 51 pontos.")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 7 Lista 4 - Tabela de Conversao de Temperaturas
#   A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = ((F - 32)* 5)/9
#   Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de
#   graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.      
    if entradaMenu == "7":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 7 - Lista 4 - Conversao Temperaturas"
        +"\nEste algoritmo converte a temperatura na escala Fahrenheit para celsius, criando uma tabela"
        +"\nonde mostrara a conversao das temperaturas a partir de 50 ate 150 graus, de grau em grau"
        +"\n---------------------------------------------------------------------------------------------")    

        tF = 50
        print("----------------------------------")
        print("Temp. Fahrenheit  -  Temp. Celsius")
        print("----------------------------------")
        while tF < 150:
            tC = ((tF - 32) * 5) / 9
            tF += 1
            print("     ",tF,"       -       %.1f" % tC)
        print("----------------------------------") 

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 8 Lista 4 - Verifica Numeros Primos
#   Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros
#   positivos dele: o 1 e o próprio n. Escreva um algoritmo que recebe um inteiro n e verica
#   se n é primo ou não.
    if entradaMenu == "8":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 8 - Lista 4 - Confirma Numeros Primos"
        +"\nEste algoritmo recebe um número do usuario e verifica se ele é um número primo."
        +"\n---------------------------------------------------------------------------------------------")    

        num = int(input("\n\nInsira um número inteiro positivo qualquer >>> "))
        divisor = 1
        contDivisores = 0
        while divisor <= num:
            resto = num % divisor
            divisor = divisor +1
            if resto == 0:
                contDivisores +=1
        if contDivisores > 2:
            print("\nO número", num, "não e primo, pois possui um total de ", contDivisores,"80divisores")
        else:
            print("\nO número", num, "é primo, pois é divisivel apenas por 1 e por ele mesmo")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 9 Lista 4 - Juros Mensais
#   Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de
#   tempo em meses t, escreva um algoritmo que calcula o valor final em dinheiro se d ficar
#   aplicado a taxa de juros j durante t meses
    if entradaMenu == "9":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 9 - Lista 4 - Calcula Juros Mensal"
        +"\nEste algoritmo calcula o valor final de um montande de dinheiro, dado uma quantidade de meses."
        +"\nque esse dinheiro ficar investido em relação a uma taxa de juros mensal"
        +"\n---------------------------------------------------------------------------------------------") 
        
        d = float(input("Informe o valor a ser aplicado no investimento: >>> R$ "))
        j = float(input("Qual a taxa de juros ao mês? (Ex: 2% = 2 / 1,9% = 1.9)>>> "))
        t = int(input("Por quantos meses voce quer deixar o dinheiro investido? >>> "))
        resultado = (d * (j/100))*t
        print("\n\nSeu investimento rendeu R$ %.2f" % resultado,"em", t, "meses, e seu saldo agora é de R$ %.2f" % (resultado + d))

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 10 Lista 4 - Calculo Fatorial
#   Escreva um algoritmo que recebe um inteiro positivo n e calcula n! = 1 · 2 · 3 . . . ·(n − 1)· n.
#   Por exemplo, se n = 6, então 6! = 1 · 2 · 3 · 4 · 5 · 6 = 720.
    if entradaMenu == "10":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 10 - Lista 4 - Calculo Fatorial"
        +"\nDado um número inteiro positivo, o algoritmo calculará seu fatorial, iniciando em 1."
        +"\n---------------------------------------------------------------------------------------------") 

        n = int(input("Digite um número inteiro positivo qualquer >>> "))
        fatorial = n
        i = 1
        calcula = 1
        n -= 1
        while n > 0:
            i += 1
            calcula *= i
            n -= 1
        print("\nO fatorial de", fatorial, "é", calcula)

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      
   
#Ex. 11 Lista 4 - Sequencia de Fibonacci
#   Escreva um algoritmo que dado n, calcula o n-ésimo número da sequência de Fibonacci
    if entradaMenu == "11":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 11 - Lista 4 - Sequencia de Fibonacci"
        +"\nO algoritmo pede ao usuario um número N, para saber qual o valor da Sequencia de Fibonacci,"
        +"\nnaquela posicao informada."
        +"\n---------------------------------------------------------------------------------------------") 

        n = int(input("Digite o número da posição da sequencia Fibonacci que deseja saber seu valor: >>> "))
        posicao = 1
        iFn1 = 1
        iFn2 = 1
        if n==1:    
            fibonacci = 1
        elif n==2:
            posicao = 2
            fibonacci = 1
        else: 
            posicao = 3
            while posicao <= n:
                fibonacci = (iFn1 - 1) + (iFn2 + 1)
                iFn2 = iFn1
                iFn1 = fibonacci
                posicao += 1
        print("\nA posição", n, "na Sequencia Fibonacci tem o valor >>>", fibonacci, "<<< !")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")      

#Ex. 12 Lista 4 - Verifica se número é Palindrome
#   Dizemos que um número natural n é palíndromo se o 1º algarismo de n é igual ao seu último
#   algarismo, o 2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente.
#   Exemplos: 567765 e 32423 são palíndromos. 567675 não é palíndromo.
    if entradaMenu == "12":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 12 - Lista 4 - Verifica se é Palíndromo"
        +"\nApós o usuario informar um número qualquer inteiro positivo, o sistema inverte os algarismos e ,"
        +"\ne verifica se o valor permanece inalterado."
        +"\n---------------------------------------------------------------------------------------------") 

        n = input("Insira um número inteiro para verificar se é Palíndrome: >>> ")
        comparaN = int(n)
        novoN = 0
        acabou = False

        while not acabou:
            resto = int(n) % 10
            if resto == 0:
                acabou = True
            else:
                n = int(n) // 10
                novoN = novoN * 10 + resto

        if comparaN == novoN:
            print("\n\nO número", comparaN, "é PALÍNDROME, pois sua inversão resulta em", novoN)
        else:
            print("\n\nNúmero não Palíndrome, pois", novoN, "é diferente de", comparaN)

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  

#Ex. 13 Lista 4 - Jogo de Advinhação
#   Vamos escrever um programa que consiste em um Jogo de Adivinhação. O jogo funciona do
#   seguinte modo: sorteia-se um número inteiro aleatório entre 1 e 1000. Sua tarefa é tentar
#   adivinhar o número sorteado através de "chutes". A cada chute o programa deverá informar
#   se o número "sorteado"é maior, menor ou igual ao número "chutado". Quando o usuário
#   acertar o número deverá ser impresso uma mensagem dizendo que ele acertou e a quantidade
#   de chutes dados. 
    if entradaMenu == "13":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 13 - Lista 4 - Jogo de Advinhacao"
        +"\nO algoritmo gera um numero aleatório entre 1 e 1000, e o usuario tem que tentar advinhar qual o"
        +"\nnumero foi gerado no sistema"
        +"\n---------------------------------------------------------------------------------------------") 

        sorteado = random.randint(1, 1001)
        chute = int(input("\nQual número voce acha que foi sorteado? Informe aqui >>> "))
        tentativas = 1
        while chute != sorteado:
            if chute > sorteado:
                print("\nChutou alto....O número sorteado é menor, tente novamente!")
                chute = int(input("Tente outro número >>> "))
            else:
                print("\nXiii..aumente um pouco mais, o numero sorteado é maior!")
                chute = int(input("Tente outro número >>> "))
            tentativas += 1
        print("\n\n::::::::::::::::::::::::::::::::::::PARABÉNS::::::::::::::::::::::::::::::::::::"
            +"\n:::::::::::::::NA MOSCA! Voce acertou o número, com" , tentativas, "tentativas:::::::::::::::"
            +"\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  
#Ex. 14 Lista 4 - Numeros Perfeitos
#   Sua tarefa será a de escrever um algoritmo em Python que, dado um inteiro positivo n,
    if entradaMenu == "14":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 14 - Lista 4 - Numeros Perfeitos"
        +"\nO algoritmo deverá encontrar os divisores de um número n inteiro, soma-los e então verificar se "
        +"\nn eh ou nao, um numero perfeito"
        +"\n---------------------------------------------------------------------------------------------") 
        num = int(input("Informe um número inteiro positivo, para descobrir se ele é Perfeito ou não >>> "))
        n=num
        divisor = 1
        somaDivisor = 0
        while divisor <= num:
            resto = num % divisor
            divisor = divisor +1
            if resto == 0:
                somaDivisor = (somaDivisor + (divisor - 1))

        resultado = somaDivisor - n
        if resultado == n:
            print("\nO numero", n, "eh um numero Perfeito!")
        else:
            print("\nO número", n, "NAO eh um numero Perfeito")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  

#Ex. 15 Lista 4 - Segmento Crescente
#   Dados um inteiro n e uma seqüência de n números inteiros, determinar o comprimento de um segmento
#   crescente de comprimento máximo.

    if entradaMenu == "15":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 15 - Lista 4 - Segmento Crescente"
        +"\nDados um inteiro n e uma seqüência de n números inteiros, determinar o comprimento de um segmento"
        +"\ncrescente de comprimento máximo. "
        +"\n---------------------------------------------------------------------------------------------") 

        n = int(input("Insira q quantidade máxima de numeros inteiros que existirão na Sequencia >>> "))
        i = 2
        contador = 1
        contMax = 0
        antigo = 0
        atual = int(input("Digite um número >>> "))
        while i <= n:
            i += 1
            antigo = atual
            atual = int(input("Digite um número >>> "))
            if atual < antigo:
                if contador > contMax:
                    contMax = contador
                    contador = 1
            else:
                contador += 1
        print("\n\nA maior sequencia foi de", contMax, "numeros")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  

#Ex. 16 Lista 4 - Calculo de Dígito com metodo de Módulo 10
#   Escreva um algoritmo que lê um número inteiro positivo e calcula o seu dígito de controle
#   usando o método do módulo 10.

    if entradaMenu == "16":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 16 - Lista 4 - Calculo de Dígito com metodo de Modulo  10"
        +"\nO Algoritmo calcula o digito verificador de uma numeração, através da metodologia do Modulo 10"
        +"\n---------------------------------------------------------------------------------------------") 

        n = int(input("Informe uma numeracao para calculo do seu digito >>>"))
        backup = n
        intercala = False
        acumula = 0
        while n > 0:
            x = n % 10
            n = n // 10
            if not intercala:
                x = x * 2
                if x >= 10:
                    x = x % 10 + x // 10
                    acumula += x
                else:
                    acumula += x
                intercala = True
            else:
                x = x * 1
                if x >= 10:
                    x = x % 10 + x // 10
                    acumula += x
                else:
                    acumula += x
                intercala = False
        fatorDigito = acumula % 10
        if fatorDigito == 0:
            digito = 0
        else:
            digito = 10 - fatorDigito
        nroCompleto = backup * 10 + digito
        print("\n\nO digito verificador da numeração informada é", digito)
        print("A numeracao completa é", nroCompleto)      

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  

#Ex. 17 Lista 4 - Calcular Raiz Quadrada
#    encontrar a raiz quadrada de um número por tentativa e erro, ou seja, seu algoritmo
#    recebe um número real n > 0 e tenta encontrar sua raiz quadrada

    if entradaMenu == "17":
        print("\n---------------------------------------------------------------------------------------------"
        +"\nEx. 17 - Lista 4 - Calcular Raiz Quadrada"
        +"\nO Algoritmo calcula a Raiz Quadrada (exata e não exata) do número informado pelo usuario, sem usar"
        +"\no método ou funcao existente no Python"
        +"\n---------------------------------------------------------------------------------------------") 

        n = float(input("\nInforme um número, para saber sua raiz quadrada: >>> "))
        buscaRaiz = n / 2
        pot = buscaRaiz * buscaRaiz
        while pot > n:
            buscaRaiz = buscaRaiz / 2
            pot = buscaRaiz * buscaRaiz
        while pot < n:
            buscaRaiz += 0.5
            pot = buscaRaiz * buscaRaiz
        print("\n\nO Resultado para a Raiz Quadrada do número", n, "é %.2f" % buscaRaiz)

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")  
        17
    else:
        print("\n---------------------------------------------------------------------------------------------")
        print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::"+
            "\n                      Selecione uma das opções no Menu abaixo!")
print("---------------------------------------------------------------------------------------------")
   