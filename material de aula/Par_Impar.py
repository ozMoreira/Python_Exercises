aux = input("escreva um numero>>> ")

num = int(aux)
resto = num % 2
if resto == 0:
    print (num, "é PAR")    
else:
    print (num,"é IMPAR")