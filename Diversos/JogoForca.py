def valida(choose, secret, letter):
    resp = ''
    i = 0
    while i < len(choose):
        if choose[i] == letter or choose[i] == letter.upper():
            resp = resp +  choose[i] + ' '
        else:
            resp = resp +  secret[i*2] + ' '
        i += 1
    return resp

def inicia_segredo(choose):
    resp = ''
    for traco in sorteada:
        if traco == ' ':
            segredo += '- '
        else:
            segredo += '_ '
    return resp
#inicializa o jogo
max_erros = int(input("\n\nInforme a quantidade máxima possível de erros >>> "))
conta_erros = 0
letra_jogada = ''

#sorteio da palavra
sorteada = "Suzuki"
segredo = inicia_segredo(sorteada)


while conta_erros < max_erros and '_' in segredo:
    print("\n",segredo)
    print("Erros: ", conta_erros)
    print("Letras já usadas: " + letra_jogada)

    letra = input("\nInforme uma letra >>> ")
    letra_jogada += letra + ' '
    segredo = valida(sorteada, segredo, letra)
    if not letra.upper() in sorteada.upper():
        conta_erros = conta_erros + 1

if conta_erros >= max_erros:
    print("\n\nVoce foi enforcado!")
    print("A palavra era, " , sorteada)
else:
    print("\n\nParabéns, voce acertou a palavra com apenas {} erros" .format(conta_erros))