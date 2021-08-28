import getpass
import os

def autentica(login, senha):
    usuarios = ('admin', 'joao', 'pedro', 'marco', 'marta')
    senhas = ('ohb8ai', 'raipa5', '12345', 'hee2oo', 'waez6d')
    i = 0
    while i < len(usuarios):
        if usuarios[i] == login:
            if senhas[i] == senha:
                return 0
            else: 
                return 1
        i = i+1
    return 2

foi = False
tentativas = 0
while not foi and tentativas < 3:
    login = input("\nUSUARIO: >>> ")
    senha = getpass.getpass("SENHA: >>>>> ")
    clear = lambda: os.system('clear')
    clear()    
    resp = autentica(login, senha)
    tentativas = tentativas + 1
    saldo = 3 - int(tentativas)
    if resp == 0:
        foi = True
    elif resp == 1:
        print("Senha invalida"
        "\nATENÇÃO! RESTAM APENAS "+ str(saldo) + " tentativas"
        "\n\nInforme novamente os dados para login!")
    elif resp ==2:
        print("Login ou Senha Invalidos"
        "\nATENÇÃO! RESTAM APENAS "+ str(saldo) + " tentativas"
        "\n\nInforme novamente os dados para login!")
    
if foi:
    print("Autenticado com sucesso")
else:
    
    print("Voce excedeu o numero de tentativas!")