print("\n---------------------------------------------------------------------------------------------\n  Exemplo de Calculo de Velocidade Média, desenvolvido como exercício da Disciplina de\nComputational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!\n--------------------------------------------------------------------------------------------- ")
distancia = input("\nInforme o uma distancia qualquer a ser percorrida em METROS. >>>> ")
tempo = input("Informe agora o tempo gasto pra percorrer essa distancia em SEGUNDOS >>> ")
mediaMS = float(distancia)/float(tempo)
converteKM = float(distancia) / 1000
converteHora = float(tempo) / 3600
mediaKmH = float(converteKM) / float(converteHora)
print("\n\nResultado em m/s\nEm", tempo,"segundos, percorre-se a distancia de", distancia," metros, na média de", mediaMS,"m/s.\n\nResultado em Km/h\nEm", converteHora," horas, percorre-se a distancia de", converteKM," metros, na média de", mediaKmH,"Km/h.\n---------------------------------------------------------------------------------------------")