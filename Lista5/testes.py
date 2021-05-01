
def isEncaixa(nA, nB):
    newN1 = 0
    if nA == nB:
        newN1 = nA
    return newN1 == nB 

def isEncaixaBA(nA, nB):
    newN1 = 0
    algA = nA
    contAlgA = 0
    contador = 0
    if nB > 100:
        nB = nB % 1000
    while algA != 0:
        restoAlga = algA % 10
        algA = algA // 10
        contAlgA += 1
    restoA = nA % 1000  
    if nA != nB:
        while contador < contAlgA:
            if newN1 != nB:
                if restoA != nB:
                    restoA = nA % 10
                    nA =  nA // 10
                    if restoA == nB % 10 and newN1 == 0:
                        newN1 = restoA
                    elif restoA != nB % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == (nB // 10) % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10
                        
                    elif restoA == (nB // 100):
                        newN1 = newN1 + restoA * 100  
                else:
                    if restoA == nB and newN1 == 0:
                        newN1 = restoA   
                    elif restoA == nB % 1000 and newN1 == 0:
                        newN1 = restoA  
                    elif restoA != nB % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == (nB // 10) % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10   
                    elif restoA == (nB // 100):
                        newN1 = newN1 + restoA * 100   
            contador +=1   
        return newN1 == nB    

def isEncaixaAB(nA, nB):
    newN1 = 0
    algA = nB
    contAlgA = 0
    contador = 0
    if nA > 100:
        nA = nA % 1000
    while algA != 0:
        restoAlga = algA % 10
        algA = algA // 10
        contAlgA += 1
    restoA = nB % 1000  
    if nB != nA:
        while contador < contAlgA:
            if newN1 != nA:
                if restoA != nA:
                    restoA = nB % 10
                    nB =  nB // 10
                    if restoA == nA % 10 and newN1 == 0:
                        newN1 = restoA
                    elif restoA != nA % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == (nA // 10) % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10
                        
                    elif restoA == (nA // 100):
                        newN1 = newN1 + restoA * 100  
                else:
                    if restoA == nA and newN1 == 0:
                        newN1 = restoA   
                    elif restoA == nA % 1000 and newN1 == 0:
                        newN1 = restoA  
                    elif restoA != nA % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == (nA // 10) % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10   
                    elif restoA == (nA // 100):
                        newN1 = newN1 + restoA * 100   
            contador +=1   
        return newN1 == nA    
        
nA = int(input("Informe uma numeracao qualquer para nA: >>> "))
nB = int(input("Informe uma numeracao qualquer para nB: >>> "))

if isEncaixa(nA, nB) or isEncaixaBA(nA, nB)== True:
    print("\n\nA numeracao de B", nB, "eh uma sequencia da numeracao de A", nA)
elif isEncaixaAB(nA, nB)== True:
    print("\n\nA numeracao de A", nA, "eh uma sequencia da numeracao de B", nB)
else:
    print("\n\nOs números não possuem sequencia")

