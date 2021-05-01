def isEncaixa(nA, nB):
    newN1 = 0
    if nA >= nB:
        
        if nB > 100:
            restoA = nA % 1000
            novoA = nA// 10
            #restoB = nB % 10
            while novoA != 0:
                
                if restoA != nB:
                    restoA = nA % 10
                    nA =  nA // 10
                    print('4 - resto N1', restoA)
                    print('4 - nB N2', nB)
                    if restoA == nB % 10 and newN1 == 0:
                        newN1 = restoA
                    elif restoA != nB % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == nB % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10
                    elif restoA == (nB // nB):
                        newN1 = newN1 + restoA * 100    
                    
                    print('4 - NEW N1', newN1)
                else:
                    if restoA == nB % 10 and newN1 == 0:
                        newN1 = restoA
                    elif restoA != nB % 10 and newN1 == 0:
                        newN1 = 0
                    elif restoA == nB % 10 and newN1 > 0 and newN1 < 10:
                        newN1 = newN1 + restoA * 10
                    elif restoA == (nB // nB):
                        newN1 = newN1 + restoA * 100    
                    print('4 - NEW N1', newN1)


            

                    return newN1 == nB






            
        #if restoA == restoB:
            
        #    return True
nA = 1545
nB = 154
print(isEncaixa(nA, nB))
#print('printA', nA)
#print('printB',nB)
        
'''restoA = nA % 10
        nA =  nA // 10
        restoB = nB % 10
        print('restoA', restoA)
        print('restoB',restoB)
        while nA % 1000 != nB:
            restoA = nA % 1000
            nA =  nA // 1000
            
            print('printA', nA)
            print('printB', nB % 1000)
        while nA % 1000 == nB % 1000:
            restoA = nA % 1000
            nA =  nA // 1000
            restoB = nB % 1000
            nB= nB // 1000
           
            contador +=1
            print('restoigualA', restoA)
            print('restoigualB',restoB)
        return restoA == restoB

    elif nA <= nB:
        restoB = nB % 10
        nB =  nB // 10
        restoA = nA % 10
     
        while restoB != restoA:
            restoB = nB % 10
            nB = nB//10
       
            
            print('printA', restoA)
            print('printB',restoB)
        while restoB == restoA:
            restoA = nA % 10
            nA= nA // 10
            restoB = nB % 10
            nB =  nB // 10
            contador +=1
        return restoB == restoA
   

nA = 1545
nB = 154
if isEncaixa(nA, nB) == True and nA > nB:
    print('\n\no numero B', nB, 'eh um segmento do numero A', nA)
elif isEncaixa(nA, nB) == True and nA < nB:
    print('\n\no numero A', nA, 'eh um segmento do numero B', nB)
else:
    print("\n\nNão existem segmentos nos números informados ")


'''
