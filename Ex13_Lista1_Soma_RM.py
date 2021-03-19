print("\n---------------------------------------------------------------------------------------------")
print("  Exemplo calculo de média final da faculdade, desenvolvido como exercício da Disciplina de")
print("Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!")
print("---------------------------------------------------------------------------------------------")

nac = input("\n                     Informe a nota da avaliaçao NAC: >>> ")
am = input("                     Informe a nota da avaliaçao AM: >>> ")
ps = input("                     Informe a nota da avaliaçao PS: >>> ")

nacPeso = float(nac)*2
amPeso = float(am)*3
psPeso = float(ps)*5

mediaFinal = (float(nacPeso) + float(amPeso) + float(psPeso))/10

print("\n                          Sua média final foi", mediaFinal,"!")
print("---------------------------------------------------------------------------------------------")