aux = input("Informe um numero")
num = int(aux)
div = 1

while div <= num:
    if num % div ==0:
        print(div)  
    div += 1
