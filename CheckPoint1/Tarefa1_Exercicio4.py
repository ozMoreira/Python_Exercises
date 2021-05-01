print("")
print("------------------------------------------------------------------------------------------------------------------")
print("|  Este é o exercicio 01 da Lista de CheckPoint #1, da disciplina de Computational Thinking do Curso de Analise  |")
print("|                            e Desenvolvimento de Sistemas da FIAP - Turma 1TDSR 2021                            |")
print("------------------------------------------------------------------------------------------------------------------")
print("\nNeste exercicio iremos calcular o valor de uma conta de água, com base no seu consumo atual x consumo anual médio\npassado, aplicando o devido desconto ou a devida multa.")

mdCnsmAnoPassado = float(input("\n\nEscreva a média de Consumo do ano passado em m3: "))
consumoMes = float(input("Escreva  consumo do mês presente em m3: "))

if consumoMes <= 20:
    valorConsumo = consumoMes * 2
elif consumoMes > 20 and consumoMes <= 35:
    valorConsumo = consumoMes * 3.5
elif consumoMes > 35 and consumoMes <= 50:
    valorConsumo = consumoMes * 5.5
else:
    valorConsumo = consumoMes * 7
print("\nValor do Consumo R$ %.2f" % valorConsumo)

if consumoMes == mdCnsmAnoPassado:
    totalConta = valorConsumo
    print("O valor total da conta foi de R$ %.2f" % totalConta)
elif consumoMes < mdCnsmAnoPassado:
    desconto = valorConsumo * 20/100
    print("O valor do desconto foi de R$ %.2f" % desconto)
    totalConta = valorConsumo - desconto
    print("O total da conta foi de %.2f" % totalConta)
else:
    aumento = consumoMes - mdCnsmAnoPassado 
    if aumento > mdCnsmAnoPassado * 10/100:   
        multa = valorConsumo * 30/100
        print("O valor da multa foi de %.2f" % multa)
        totalConta = valorConsumo + multa
        print("O total da conta foi de %.2f" % totalConta)   
    else: 
        totalConta = valorConsumo


