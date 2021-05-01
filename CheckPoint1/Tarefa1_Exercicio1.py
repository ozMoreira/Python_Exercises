print("")
print("------------------------------------------------------------------------------------------------------------------")
print("|  Este é o exercicio 01 da Lista de CheckPoint #1, da disciplina de Computational Thinking do Curso de Analise  |")
print("|                            e Desenvolvimento de Sistemas da FIAP - Turma 1TDSR 2021                            |")
print("------------------------------------------------------------------------------------------------------------------")
print("\nNeste exercicio iremos calcular o salario mensal de um professor, uma vez dada valor da hora-aula e quantidade de\naulas-semanais, ambos dados pelo usuario")

aulasPorSemana = int(input("\nDigite o número de aulas por semana: "))
valorHoraAula = float(input("\nDigite o valor da hora-aula: "))

salarioBase = aulasPorSemana * 4.5 * valorHoraAula
horaAtividade = salarioBase * 0.05
dsr = (salarioBase + horaAtividade) * 1/6
salarioMensal = salarioBase + horaAtividade + dsr

print("\nO valor do salario base é de R$ %.2f"  % salarioBase)
print("O valor da hora-atividade é de R$ %.2f" % horaAtividade)
print("O valor de descanso semanal remunerado é de R$ %.2f" % dsr)
print("Por tanto o salário mensal é de R$ %.2f" % salarioMensal)