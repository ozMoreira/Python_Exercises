print("\n-----------------------------------------------------------------------------------------------------------\n  Seja bem vindo ao sistema de calculo de Circunferencia e Área Circular, desenvolvido como exercício da\nDisciplina de Computational Thinking do Curso de Analise e Desenvolvimento de Sistemas da FIAP turma 2021!\n----------------------------------------------------------------------------------------------------------- ")
raio = input("\nPara calcular a área de um Círculo, precisamos multiplicar o Raio deste circulo por \u03C0. elevado ao quadrado.\nInforme o raio do seu círculo, para efetuarmos o calculo: >>> ")
pi = 3.14
area = pi*float(raio)**2
perimetro = 2*pi*float(raio)
print("\n...calculando...\n\nA área do circulo informado é >>>",(area),"<<<\n-----------------------------------------------------------------------------------------------------------")
print("\nConsiderando agora o mesmo raio, calcularemos a circunferencia, sabendo que o perímetro da circunferência é\ndado pelo dobro do produto do raio por \u03C0")
print("\n...calculando...\n\nO perímetro do circulo informado é >>>",(perimetro),"<<<\n-----------------------------------------------------------------------------------------------------------")
