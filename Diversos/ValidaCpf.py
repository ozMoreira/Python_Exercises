aux = int(input("Insira um número de CPF: >>> "))
aux2 = str(aux)
'''
#Separa o CPF, separando em 4 partes!
digito = (cpf % 100)
cpf = cpf // 100
tripla3 = cpf % 1000
cpf = cpf // 1000
tripla2 = cpf % 1000
cpf = cpf // 1000
tripla1 = cpf % 1000
cpf = cpf // 1000

#Formata e imprimi o CPF separando em 4 partes!
parte4 = "{:02}".format(digito)
parte3 = "{:03}".format(tripla3)
parte2 = "{:03}".format(tripla2)
parte1 = "{:03}".format(tripla1)
print(parte1 + "." + parte2 + "." + parte3 +  "-" + parte4)
'''
ac = 0
multp = 2
while aux !=0:
    dig = aux % 10
    aux = aux // 10
    ac = ac + dig * multp
    multp = multp + 1
    '''
    print("Digito", dig)
    print("CPF RESTANTE", aux)
    print("Acumulador", ac)
    print("Multp", multp)
    '''
resto = ac % 11
if resto < 2:
    print("Digito vale 0")
    dv1 = 0
else:
    dv1 = 11 - resto
    print("Digito vale " , dv1)


dv1Str = str(dv1)
aux2 = str(aux2 + dv1Str)
cpf2 = int(aux2)    
print(cpf2)
ac2 = 0
multp2 = 2
while cpf2 !=0:
    dig2 = aux % 10
    cpf2 = aux // 10
    ac2 = ac2 + dig2 * multp2
    multp2 = multp2 + 1

resto2 = ac2 % 11
if resto2 < 2:
    print("Digito vale 0")
    dv2 = 0
else:
    dv2 = 11 - resto2
    print("Digito vale " , dv2)

dv2Str = str(dv2)
cpfFinal = str(cpf2)
print("CPF FINAL", cpfFinal + dv2Str)



    
 
    

