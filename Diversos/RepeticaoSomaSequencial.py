aux = int(input("Digite um numero"))

n = aux
num = 0
i = 1

while num <= n:
    num += num + i
    i += 1
    #
    print (num)

    #num += 1
print (num)