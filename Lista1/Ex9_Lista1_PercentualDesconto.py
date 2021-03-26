print("\n---------------------------------------------------------------------------------------------\n  Exemplo de Percentual de Desconto aplicado, desenvolvido como exercício da Disciplina de\nComputational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!\n--------------------------------------------------------------------------------------------- ")
valorProduto = input("\nInforme o valor do produto, que receberá o desconto. (Ex: R$ 50.00) >>>> R$ ")
percentual = input("Informe agora o PERCENTUAL que será aplicado. (Ex: 50 = 50%) >>> ")
calculaPercent = (float(valorProduto)*float(percentual))/100
aplicaDesconto = float(valorProduto) - float(calculaPercent)
acrescentaPercent = float(valorProduto) + float(calculaPercent)
print("\nO produto tem valor original de R$", valorProduto,". Caso seja aplicado desconto de", percentual,"% \no novo Preço será de R$",float(aplicaDesconto), "Caso seja aplicado uma adição percentual, o Preço será R$",float(acrescentaPercent),".\n---------------------------------------------------------------------------------------------")