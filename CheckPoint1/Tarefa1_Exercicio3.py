import math
print("")
print("------------------------------------------------------------------------------------------------------------------")
print("|  Este é o exercicio 01 da Lista de CheckPoint #1, da disciplina de Computational Thinking do Curso de Analise  |")
print("|                            e Desenvolvimento de Sistemas da FIAP - Turma 1TDSR 2021                            |")
print("------------------------------------------------------------------------------------------------------------------")
print("\nNeste exercicio iremos o valor final de uma conta de luz!\n\n")

consumoMensal = int(input("Digite o valor do consumo mensal em kWh: "))

if consumoMensal < 51:
    valorConsumo = 14
else:
    valorConsumo = 14 + consumoMensal * 0.25
print("\nO valor do consumo é: R$ %.2f" % valorConsumo)

if consumoMensal <= 99:
    icms = 0
elif consumoMensal >= 100 and consumoMensal <= 200:
    icms = valorConsumo * 13/100
else:
    icms = valorConsumo * 33/100

valorFinal = valorConsumo + icms
print("O valor do ICMS é: R$ %.2f" % icms)
print("O total da conta é: R$ %.2f" % valorFinal)

