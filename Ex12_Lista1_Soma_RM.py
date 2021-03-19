print("\n---------------------------------------------------------------------------------------------")
print("  Exemplo desmembramento de milhar com módulo, desenvolvido como exercício da Disciplina de")
print("Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!")
print("---------------------------------------------------------------------------------------------")

x = input("\n Informe o número do seu RM: >>>")

n1 = int(x)/10000 
n2 = (int(x)/1000)%10 
n3 = (int(x)/100)%10 
n4 = (int(x)/10)%10 
n5 = int(x)%10 
soma = (int(n1) + int(n2) + int(n3) + int(n4) + int(n5))

print("...Desmembrando algarismos em", int(n1), int(n2), int(n3), int(n4), int(n5),"\n...Processando...")
print("\n Sua matrícula RM", x,"resulta em ", soma, "quando somamos seus algarismos!")
print("---------------------------------------------------------------------------------------------")