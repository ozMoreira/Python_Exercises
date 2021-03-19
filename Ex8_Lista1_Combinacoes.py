print("\n---------------------------------------------------------------------------------------------\n       Exemplo de Analise Combinatoria, desenvolvido como exercício da Disciplina de\nComputational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!\n--------------------------------------------------------------------------------------------- ")
print("\n A  * ANALISE COMBINATÓRIA *  verifica as possíveis combinações entre umconjunto de elementos.\nPortanto, para resolvermos um problema, basta multiplicarmos o número de opções entre\nas escolhas apresentadas. Vamos calcular as posasiveis combinações de roupa agora, por ex:")

camisetas = input("\n\n- Informe o número (inteiro) de camisetas que deseja combinar: >>> ")
calcas = input("- Informe agora a quantidade de calças que combinaremos: >>> ")
sapatos = input("- Informe quantos pares de sapatos usaremos na combinação: >>> ")
analiseCombinatoria = int(camisetas)*int(calcas)*int(sapatos)

print("\n\nPara o total de", camisetas,"camisetas,", calcas,"calças e", sapatos, "pares de calçados, voce terá um\ntotal de >>>",analiseCombinatoria,"<<< possiveis combinações de vestuário.\n---------------------------------------------------------------------------------------------")