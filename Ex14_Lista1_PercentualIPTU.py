print("\n---------------------------------------------------------------------------------------------")
print("    Exemplo calculo de Desconto no IPTU, desenvolvido como exercício da Disciplina de")
print("Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!")
print("---------------------------------------------------------------------------------------------")

unicaParcela = input("\nInforme o valor do IPTU, para pagamento à vista: >>>> R$ ")
parcelado = input("Informe o valor de cada parcela do carnê do IPTU: >>> R$ ")
iptuTotalParcelado = float(parcelado)*10
print("O valor do iptu ai termino das parcelas será de R$", iptuTotalParcelado,)
diferencaPagamento = (float(iptuTotalParcelado)-float(unicaParcela))
percentual = (float(diferencaPagamento)/float(unicaParcela))*100
print("\nO desconto aplicado, para o pagamento à vista, foi de",percentual,"%" "em relação ao parcelado!")
print("---------------------------------------------------------------------------------------------")