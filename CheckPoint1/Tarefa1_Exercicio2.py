print("")
print("------------------------------------------------------------------------------------------------------------------")
print("|  Este eh o exercicio 02 da Lista de CheckPoint #1, da disciplina de Computational Thinking do Curso de Analise |")
print("|                            e Desenvolvimento de Sistemas da FIAP - Turma 1TDSR 2021                            |")
print("------------------------------------------------------------------------------------------------------------------")
print("\nNeste exemplo iremos somar uma dada quantidade de MESES, a uma Idade/Periodo qualquer, ambos dados pelo usuario")

entrada = int(input("\nInforme um numero qualquer que represente um periodo de ANOS (Ex. 1 ano, 2 anos, 3 anos....)  >>> "))
ano = entrada
entrada = int(input("Insira agora uma quantidade de MESES, que nao ultrapasse o periodo de 11 meses  >>> "))
mes = entrada

calculaAno = 0
pegaMesRestante = 0
mesAdicional = 0
periodoValido = True

if ano < 0 or mes > 11:
    periodoValido = False

else:
    print("\n>>> ATENCAO <<<  Voce informou o periodo de", ano, "ano e", mes,"meses!")
    entrada = int(input("\nQuantos MESES voce quer adicionar ou Subtrair ao periodo informado? (Ex. 13 meses, -27 meses, 53 meses...)   >>> "))
    mesAdicional = entrada

if mesAdicional > 0:
    calculaAno = ano
    pegaMesRestante = ((ano * 12)+mes) + mesAdicional
    if pegaMesRestante == 12:
        calculaAno += int(pegaMesRestante / 12) 
        pegaMesRestante = 0
    elif pegaMesRestante > 12:
        calculaAno = int(pegaMesRestante / 12)
        pegaMesRestante %= 12
    
else:
    calculaAno = ano
    pegaMesRestante = ((ano * 12)+mes) + mesAdicional
    if pegaMesRestante == 12:
        calculaAno += int(pegaMesRestante / 12) 
        pegaMesRestante = 0
    elif pegaMesRestante > 12:
        calculaAno = int(pegaMesRestante / 12)
        pegaMesRestante %= 12

if periodoValido == True:
    print("\nA nova idade eh de", calculaAno, "ano(s) e ", pegaMesRestante,"mes(es)!")
else:
    print("\n\n>>> ATENCAO<<< --- ERRO!!! --- Ano informado foi negativo ou o primeiro período de meses foi superior a 11 meses!")