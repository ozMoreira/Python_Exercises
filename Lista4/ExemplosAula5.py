n = float(input("\nInforme um número, para saber sua raiz quadrada: >>>"))
buscaRaiz = n / 2
pot = buscaRaiz * buscaRaiz
while pot > n:
    buscaRaiz = buscaRaiz / 2
    pot = buscaRaiz * buscaRaiz
while pot < n:
    buscaRaiz += 0.5
    pot = buscaRaiz * buscaRaiz
print("\n\nO Resultado para a Raiz Quadrada do número", n, "é %.2f" % buscaRaiz)