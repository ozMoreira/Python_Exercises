print("")
print("------------------------------------------------------------------------------------------------------------------")
print("|  Este é o exercicio 01 da Lista de CheckPoint #1, da disciplina de Computational Thinking do Curso de Analise  |")
print("|                            e Desenvolvimento de Sistemas da FIAP - Turma 1TDSR 2021                            |")
print("------------------------------------------------------------------------------------------------------------------")
print("\nNeste exercicio iremos calcular o valor da contribuição de um colaborador, dado seu salário x tabela de progressão")

salarioContribuicao = float(input("\n\nDigite o salário de contribuição: R$ "))

if salarioContribuicao >= 3305.23:
    contribuicao = ((salarioContribuicao - 3305.22) * 14/100) + ((3305.22 - 2203.48) * 12/100) + ((2203.48 - 1100) * 9/100) + (1100 * 7.5/100)
elif salarioContribuicao <= 3305.22 and salarioContribuicao >= 2203.49:
    contribuicao = ((salarioContribuicao - 2203.48) * 12/100) + ((2203.48 - 1100) * 9/100) + (1100 * 7.5/100)
elif salarioContribuicao <= 2203.48 and salarioContribuicao >= 1100:
    contribuicao = ((salarioContribuicao - 1100) * 9/100) + (1100 * 7.5/100)
else:
    contribuicao = salarioContribuicao * 7.5/100

print("O valor da contribuição, será no valor de R$ %.2f" % contribuicao)

