
entrada = float(input("\n Informe a média do Primeiro Semestre >>> "))
sem1 = entrada
entrada = float(input("\n Informe a média do Segundo Semestre  >>> "))
sem2 = entrada
entrada = float(input("\n Quantas aulas o aluno assistiu no total?  >>> "))
aulasAluno = entrada
entrada = float(input("\n Quantas aulas foram apresentadas no total??  >>> "))
aulasProf = entrada
     
sem1Peso = sem1 * 4

sem2Peso = sem2 * 6
mediaFinal = (sem1Peso + sem2Peso)/10
percentEvasaoAluno = ((aulasProf-aulasAluno)/aulasAluno)*100
nFaltas = aulasProf - aulasAluno
presencaValidada = 100 - percentEvasaoAluno

if (mediaFinal > 6 and presencaValidada > 70):
    print("\n\nfoi APROVADO com média final {:.2f}" .format(mediaFinal), "e participou de {:.2f}" .format(presencaValidada),"% das aulas")
elif (mediaFinal >= 4 and mediaFinal <= 5.9 and presencaValidada > 70):
    print("\n\nterá que ficar de EXAME, pois está com Média Final {:.2f}" .format(mediaFinal), " mesmo participando de {:.2f}" .format(presencaValidada),"% das aulas")
elif (mediaFinal < 4 and presencaValidada > 70):
    print("\n\nfoi REPROVADO, pois está com Média Final {:.2f}" .format(mediaFinal), " mesmo participando de {:.2f}" .format(presencaValidada),"% das aulas")
elif ( mediaFinal > 4 and presencaValidada < 70 ):
    print("\n\nestá REPROVADO por falta, pois compareceu apenas a {:.2f}" .format(presencaValidada),"% do total de", aulasProf, "aulas, independente de sua Média Final que foi {:.2f}".format(mediaFinal))
