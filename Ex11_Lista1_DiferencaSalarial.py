print("\n---------------------------------------------------------------------------------------------")
print("  Exemplo de percentual na diferença salarial, desenvolvido como exercício da Disciplina de")
print("Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!")
print("---------------------------------------------------------------------------------------------")

salarioAntigo = input("\nInforme o salario antes do aumento. >>>> R$ ")
salarioAtual = input("Informe o salario atual >>> R$ ")
diferenca = float(salarioAtual) - float(salarioAntigo)
##calcula a divisão dos salarios, pelo salario antigo, e acha o percentual multiplicando por 100.
percentual = float(diferenca)/float(salarioAntigo)*100

print("\nResultado:\nO salario teve um aumento de",percentual,"%.")
print("---------------------------------------------------------------------------------------------")