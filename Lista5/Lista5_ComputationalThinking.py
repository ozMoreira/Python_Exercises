entradaMenu = "999"
while entradaMenu != "0":
    print("\n---------------------------------------------------------------------------------------------"
        +"\n         Seja bem vindo à QUINTA LISTA DE EXERCÍCIOS de COMPUTATIONAL THINKING USING PYTHON"
        +"\n---------------------------------------------------------------------------------------------"
        +"\nDigite uma das opções do menu abaixo para acessar o exercicio:"
        +"\n1 - Valida Numero Primo"
        +"\n2 - Primos de 2 a 100"
        +"\n3 - Numeros Perfeitos de 1 a 50k"
        +"\n4 - Valida Permutacao"
        +"\n5 - Compara Números"
        +"\n0 - SAIR")
    entradaMenu = input("\nDigite sua opção de menu aqui >>> ")

#Ex. 1 - Lista 5 - Retorna True se N for um Numero Primo
#    Escreva uma função que recebe um inteiro n e retorna o valor True se n é primo ou False se ele não for primo.
    if entradaMenu =="1":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 1 - Lista 5 - Valida Numero Primo"
            +"\nAlgoritmo pede pro usuario informar um numero inteiro N, e valida se eh ou nao um numero primo"
            +"\n\n---------------------------------------------------------------------------------------------")

        def isPrimo(n):
            divisor = 1
            contDivisores = 0
            while divisor <= n:
                resto = n % divisor
                divisor = divisor +1
                if resto == 0:
                    contDivisores +=1

            if contDivisores > 2:
                return False
            else:
                return True 
            return contDivisores

        num = int(input("\n\nInsira um número inteiro positivo qualquer >>> "))

        if isPrimo(num) == True:
            print(isPrimo(num),'---> O numero', num, 'Eh Primo, pois seus divisores são 1 e ele mesmo')
        else:
            print(isPrimo(num),'---> O numero', num, 'NAO eh Primo, pois possui mais divisores além de 1 e ele mesmo')
                
        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     
    
#Ex. 2 - Lista 5 - Imprime os 100 primeiros números primos
#    escreva um programa que imprime os 100 primeiros números primos começando do número 2
    if entradaMenu =="2":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 2 - Lista 5 - 100 primeiros primos"
            +"\nAlgoritmo parte do número primo 2, para imprimir os 100 primeiros primos"
            +"\n\n---------------------------------------------------------------------------------------------")
        
        def isPrimo(n):
            divisor = 1
            contDivisores = 0
            while divisor <= n:
                resto = n % divisor
                divisor = divisor +1
                if resto == 0:
                    contDivisores +=1

            if contDivisores > 2:
                return False
            else:
                return True 
            return contDivisores

        num = 2
        while num < 100:
            if isPrimo(num) == True:
                print('---> ', num)
                num += 1
            else:
                num += 1

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")    

#Ex. 3 - Lista 5 - Imprimi N Perfeitos de 1 a 50k
#   Usando a função que verifica se um número é perfeito ou não, escreva um algoritmo que
#   mostra todos os números perfeitos no intervalo de 1 a 50000 (cinquenta mil).

    if entradaMenu =="3":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 3 - Lista 5 - Imprime N Perfeitos de 1 a 50k"
            +"\nAlgoritmo calcula número por número e verifica se é ou não perfeito, até que chegue em N = 50k"
            +"\n\n---------------------------------------------------------------------------------------------")
        
        def isPerfeito(n):
            divisor = 1
            somaDivisor = 0
            while divisor <= n:
                resto = n % divisor
                divisor = divisor +1
                if resto == 0:
                    somaDivisor = (somaDivisor + (divisor - 1))
                resultado = somaDivisor - n
            return resultado == n
        n = 1
        while n < 50000:
            if isPerfeito(n) == True:
                print("--->", n)
                n+=1
            else:
                n+=1

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")    

#Ex. 4 - Lista 5 - Confirma Permutacao
#   faça um programa que lê dois inteiros positivos a e b e responda se a é permutação de b
    if entradaMenu =="4":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 4 - Lista 5 - Valida Permutacao"
            +"\nAlgoritmo confirma se os digitos entre Num A e Num B são permutaveis"
            +"\n\n---------------------------------------------------------------------------------------------")
        
        def contaDigitos(n, d):
            contador = 0
            while n != 0:
                resto  = n % 10
                if resto == d:
                    contador = contador + 1
                n = n // 10
            return contador

        digito = 1
        n = int(input("Informe o primeiro número >>> "))
        numA = n
        n2 = int(input("Informe o segundo número >>> "))
        numB = n2

        while digito <= 9 and contaDigitos(numA, digito) == contaDigitos(numB, digito):
            digito = digito+1

        if digito > 9:
            print("\n\n", numA, 'eh permutacao de', numB)
        else:
            print("\n\n", numA, 'nao eh permutacao de', numB)
        '''
        conta0 = 0
        conta1 = 0
        conta2 = 0
        conta3 = 0
        conta4 = 0
        conta5 = 0
        conta6 = 0
        conta7 = 0
        conta8 = 0
        conta9 = 0
        conta20 = 0
        conta21 = 0
        conta22 = 0
        conta23 = 0
        conta24 = 0
        conta25 = 0
        conta26 = 0
        conta27 = 0
        conta28 = 0
        conta29 = 0
        while (n != 0): 
            d = n % 10
            n = n // 10
            
            if d == 0:
                conta0 += 1
            elif d == 1:
                conta1 += 1
            elif d == 2:
                conta2 += 1
            elif d == 3:
                conta3 += 1
            elif d == 4:
                conta4 += 1
            elif d == 5:
                conta5 += 1
            elif d == 6:
                conta6 += 1
            elif d == 7:
                conta7 += 1
            elif d == 8:
                conta8 += 1
            elif d == 9:
                conta9 += 1

        while (n2 != 0): 
            d = n2 % 10
            n2 = n2 // 10
            
            if d == 0:
                conta2 += 1
            elif d == 1:
                conta21 += 1
            elif d == 2:
                conta22 += 1
            elif d == 3:
                conta23 += 1
            elif d == 4:
                conta24 += 1
            elif d == 5:
                conta25 += 1
            elif d == 6:
                conta26 += 1
            elif d == 7:
                conta27 += 1
            elif d == 8:
                conta28 += 1
            elif d == 9:
                conta29 += 1

        if conta0 == conta20 and conta1 == conta21 and conta2 == conta22 and conta3 == conta23 and conta4 == conta24 and conta5 == conta25 and conta6 == conta26 and conta7 == conta27 and conta8 == conta28 and conta9 == conta29:
            print("\n\nO número", numA, "eh permutacao de", numB)
        else:
            print("\n\nO número", numA, "não eh permutacao de", numB)'''

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")    

#Ex. 5 - Lista 5 - Confere Ultimos Digitos
#   Construa uma função encaixa que dados dois inteiros positivos a e b verifica se b corresponde aos
#   últimos dígitos de a
    if entradaMenu =="5":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 5 - Lista 5 - Confere Ultimos Digitos"
            +"\nAlgoritmo confirma se os digitos entre Num A e Num B são permutaveis"
            +"\n\n---------------------------------------------------------------------------------------------")

        def isEncaixa(nA, nB):
            contador = 1
            if nA >= nB:
                while contador <= 4:
                    restoA = nA % 10
                    nA =  nA // 10
                    restoB = nB % 10
                    nB= nB // 10
                    contador +=1   
                    return restoA == restoB
            return False

        nA = int(input("Informe um número qualquer >>> "))
        nB = int(input("Informe um segundo número para comparação >>> "))
        if isEncaixa(nA, nB) == True:
            print('\n\nO numero', nB, 'encaixa em', nA)
        else:
            print('\n\nO numero', nB, 'NAO encaixa em', nA)

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")    
#Ex. 6 - Lista 5 - Confere Ultimos Digitos
#   Construa uma função encaixa que dados dois inteiros positivos a e b verifica se b corresponde aos
#   últimos dígitos de a
    if entradaMenu =="6":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 6 - Lista 5 - Confere Ultimos Digitos"
            +"\nAlgoritmo confirma se os digitos entre Num A e Num B são permutaveis"
            +"\n\n---------------------------------------------------------------------------------------------")

        def isEncaixa(nA, nB):
            newN1 = 0
            if nA == nB:
                newN1 = nA
            return newN1 == nB 

        def isEncaixaBA(nA, nB):
            newN1 = 0
            algA = nA
            contAlgA = 0
            contador = 0
            if nB > 100:
                nB = nB % 1000
            while algA != 0:
                restoAlga = algA % 10
                algA = algA // 10
                contAlgA += 1
            restoA = nA % 1000  
            if nA != nB:
                while contador < contAlgA:
                    if newN1 != nB:
                        if restoA != nB:
                            restoA = nA % 10
                            nA =  nA // 10
                            if restoA == nB % 10 and newN1 == 0:
                                newN1 = restoA
                            elif restoA != nB % 10 and newN1 == 0:
                                newN1 = 0
                            elif restoA == (nB // 10) % 10 and newN1 > 0 and newN1 < 10:
                                newN1 = newN1 + restoA * 10
                                
                            elif restoA == (nB // 100):
                                newN1 = newN1 + restoA * 100  
                        else:
                            if restoA == nB and newN1 == 0:
                                newN1 = restoA   
                            elif restoA == nB % 1000 and newN1 == 0:
                                newN1 = restoA  
                            elif restoA != nB % 10 and newN1 == 0:
                                newN1 = 0
                            elif restoA == (nB // 10) % 10 and newN1 > 0 and newN1 < 10:
                                newN1 = newN1 + restoA * 10   
                            elif restoA == (nB // 100):
                                newN1 = newN1 + restoA * 100   
                    contador +=1   
                return newN1 == nB    

        def isEncaixaAB(nA, nB):
            newN1 = 0
            algA = nB
            contAlgA = 0
            contador = 0
            if nA > 100:
                nA = nA % 1000
            while algA != 0:
                restoAlga = algA % 10
                algA = algA // 10
                contAlgA += 1
            restoA = nB % 1000  
            if nB != nA:
                while contador < contAlgA:
                    if newN1 != nA:
                        if restoA != nA:
                            restoA = nB % 10
                            nB =  nB // 10
                            if restoA == nA % 10 and newN1 == 0:
                                newN1 = restoA
                            elif restoA != nA % 10 and newN1 == 0:
                                newN1 = 0
                            elif restoA == (nA // 10) % 10 and newN1 > 0 and newN1 < 10:
                                newN1 = newN1 + restoA * 10
                                
                            elif restoA == (nA // 100):
                                newN1 = newN1 + restoA * 100  
                        else:
                            if restoA == nA and newN1 == 0:
                                newN1 = restoA   
                            elif restoA == nA % 1000 and newN1 == 0:
                                newN1 = restoA  
                            elif restoA != nA % 10 and newN1 == 0:
                                newN1 = 0
                            elif restoA == (nA // 10) % 10 and newN1 > 0 and newN1 < 10:
                                newN1 = newN1 + restoA * 10   
                            elif restoA == (nA // 100):
                                newN1 = newN1 + restoA * 100   
                    contador +=1   
                return newN1 == nA    
                
        nA = int(input("Informe uma numeracao qualquer para nA: >>> "))
        nB = int(input("Informe uma numeracao qualquer para nB: >>> "))

        if isEncaixa(nA, nB) or isEncaixaBA(nA, nB)== True:
            print("\n\nA numeracao de B", nB, "eh uma sequencia da numeracao de A", nA)
        elif isEncaixaAB(nA, nB)== True:
            print("\n\nA numeracao de A", nA, "eh uma sequencia da numeracao de B", nB)
        else:
            print("\n\nOs números não possuem sequencia")

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")    

#Ex. 7 - Lista 5 - Confere Ultimos Digitos
#   Construa uma função encaixa que dados dois inteiros positivos a e b verifica se b corresponde aos
#   últimos dígitos de a
    if entradaMenu =="7":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 7 - Lista 5 - Confere Ultimos Digitos"
            +"\nAlgoritmo confirma se os digitos entre Num A e Num B são permutaveis"
            +"\n\n---------------------------------------------------------------------------------------------")

    else:
        print("\n---------------------------------------------------------------------------------------------"
        +"\n       ::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::"
        +"\n                            Selecione uma das opções no Menu abaixo!"
        +"\n---------------------------------------------------------------------------------------------")