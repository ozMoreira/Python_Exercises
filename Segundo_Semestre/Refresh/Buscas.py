def busca(vet, x):
    i = 0
    while i< len(vet)and vet[i] != x:
        i = i+1
    if i == len(vet):
        return -1
    else:
        return i

def busca2(vet, x):
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1


vet = ['fut', 'gin', 'atl', 'judo', 'tenis', 'basquete']
resp = busca(vet, 'tenis')
print(resp)

resp2 = busca2(vet, 'atl')
print(resp2)