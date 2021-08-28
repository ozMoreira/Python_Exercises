entradaMenu = "-1"
while entradaMenu != "0":
    print("\n---------------------------------------------------------------------------------------------"
        +"\n         Seja bem vindo à SEXTA LISTA DE EXERCÍCIOS de COMPUTATIONAL THINKING USING PYTHON"
        +"\n---------------------------------------------------------------------------------------------"
        +"\nDigite uma das opções do menu abaixo para acessar o exercicio:"
        +"\n1 - Caixa Alta"
        +"\n2 - Espaçador de Palavras"
        +"\n3 - Substitui Letra"
        +"\n4 - Substitui Grupos de Letras"
        +"\n5 - Busca Trecho de Frase"
        +"\n\n0 - SAIR")
    entradaMenu = input("\nDigite sua opção de menu aqui >>> ")

#ex 1 - Crie uma função em Python que recebe uma String e retorna uma outra String com os
#mesmos caracteres só que em caixa alta. Por exemplo: se a palavra for "Melancia", sua
#função deverá retornar "MELANCIA".
    if entradaMenu =="1":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 1 - Lista 6 - Caixa Alta"
            +"\nAlgoritmo retorna uma palavra qualquer digitada, formatada em caixa alta"
            +"\n---------------------------------------------------------------------------------------------")

        def caixa_alta(texto):
            return texto.upper()

        entrada = input("\nDigite uma palavra >>> ")
        print('Sua palavra formatada fica >>> ',caixa_alta(entrada))

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     

#ex2 - Crie uma função que retorna uma String contendo os caracteres do parâmetro palavra sepa-
# rados por espaços. Por exemplo, se o parâmetro passado for a palavra "Manga", seu método
# deverá retornar "M a n g a ".
    if entradaMenu =="2":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 2 - Lista 6 - Separador de Palavras"
            +"\nAlgoritmo retorna uma palavra qualquer digitada, espaçada entre suas letras"
            +"\n---------------------------------------------------------------------------------------------")
        
        def separa(texto):
            resp = ""
            for c in texto:
                resp += c + ' '
            return resp

        entrada = input("\nDigite uma palavra >>> ")
        print('Sua palavra formatada fica >>> ',separa(entrada))   
        

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     

#ex3 - Escreva uma função que recebe duas Strings: frase e letra; a frase representa um
# conjunto de caracteres e letra um único caracter. Sua função deverá substituir toda
# ocorrência do caracter letra contido frase pelo caracter *. Por exemplo, se frase for
# "Jabuticaba" e a letra for "a"então seu método deverá retornar "J*butic*b*". Note
# que, sua função deverá funcionar independente da letra ser maiúscula ou minúscula, ou seja,
# toda letra "a"e "A"deve ser substituída. Considere que não há caracteres acentuados nas
# palavras e não deve ser usado o método replace neste exercício.
    if entradaMenu =="3":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 3 - Lista 6 - Substitui letra"
            +"\nAlgoritmo retorna uma frase qualquer digitada, substituindo uma letra por *"
            +"\n---------------------------------------------------------------------------------------------")
        def caixa_alta(texto):
            return texto.upper()

        def caixa_baixa(texto):
            return texto.lower()

        def substitui(frase, letra):
            resp = ''
            letra_alta = caixa_alta(letra)
            letra_baixa = caixa_baixa(letra)
            for caract in frase:
                if caract == letra or caract == letra_alta or caract == letra_baixa:
                    resp += '*'
                else:
                    resp += caract
            return resp
        
        entradaFrase = input("\nDigite uma frase >>> ")
        entradaLetra = input("\nDigite uma letra para substituição >>> ")

        print('Sua frase formatada fica >>> ',substitui(entradaFrase, entradaLetra))

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     

#ex4 - Escreva uma função que recebe duas Strings: frase e letras; a frase representa um
# conjunto de caracteres e letras alguns caracteres. Sua função deverá substituir cada
# caracter c contido na frase pelo caracter * se este caracter c estiver presente em letras.
    if entradaMenu =="4":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 4 - Lista 6 - Substitui Grupos de Letras"
            +"\nAlgoritmo retorna uma frase qualquer digitada, subtituindo um grupo de letras por *"
            +"\n---------------------------------------------------------------------------------------------")
        
        def caixa_alta(texto):
            return texto.upper()

        def caixa_baixa(texto):
            return texto.lower()

        def substitui(frase, letra):
            resp = ''
            letra_alta = caixa_alta(letra)
            letra_baixa = caixa_baixa(letra)
            for caract in frase:
                if caract == letra or caract == letra_alta or caract == letra_baixa:
                    resp += '*'
                else:
                    resp += caract
            return resp

        def substitui_letras(frase, letras):
            i = 0
            while i < len(letras):
                frase = substitui(frase, letras[i])
                i += 1
            return frase
        
        entradaFrase = input("\nDigite uma frase >>> ")
        entradaLetras = input("\nDigite as letras para substituição >>> ")

        print('Sua frase formatada fica >>> ',substitui_letras(entradaFrase, entradaLetras))
        
        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     

#ex5- Dados duas strings (um contendo uma frase e outro contendo uma palavra), determine o
# número de vezes que a palavra ocorre na frase.
    if entradaMenu =="5":
        print("\n---------------------------------------------------------------------------------------------"
            +"\nEx. 5 - Lista 6 - Busca Trecho de Frase"
            +"\nAlgoritmo retorna o numero de vezes que uma palavra existe em uma frase!"
            +"\n---------------------------------------------------------------------------------------------")
        
        entradaFrase = input("\nDigite uma frase >>> ")
        entradaPalavra = input("\nDigite a palavra que quer encontrar na frase >>> ")
        
        pos = entradaFrase.find(entradaPalavra, 0)
        contador = 0
        while pos != -1:
            contador += 1
            pos = entradaFrase.find(entradaPalavra, pos + 1)

        print('A palavra ', entradaPalavra, ' é encontrada ', contador, 'vezes na frase informada!')

        voltaMenu = input("\n\n\nDigite '1' para retornar ao menu Principal >>> ")
        while voltaMenu != '1':
            print("::::::::::::::::::::::::::::::::::::ATENÇÃO::::::::::::::::::::::::::::::::::::")
            voltaMenu = input("                Digite '1' para retornar ao menu Principal >>> ")
        print("Obrigado pela sua visita a esta funcionalidade")     

