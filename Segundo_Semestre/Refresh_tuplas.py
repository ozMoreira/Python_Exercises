#usando 2 tuplas
usuarios = ('admin', 'joao', 'pedro', 'marco', 'marta')
senhas = ('ohb8ai', 'raipa5', 'rie4co', 'hee2oo', 'waez6d')

#usando 1 tupla
usuarios_senhas = (('admin', 'ohb8ai'), 
                  ('joao','raipa5'),
                  ('pedro', 'rie4co'), 
                  ('marco', 'hee2oo'), 
                  ('marta', 'waez6d')
                  )

def autentica(login, senha):
    usuarios = ('admin', 'joao', 'pedro', 'marco', 'marta')
    senhas = ('ohb8ai', 'raipa5', 'rie4co', 'hee2oo', 'waez6d')
    i = 0
    while i < len(usuarios):
        if usuarios[i] == login:
            if senhas[i] == senha:
                return 0
            else: 
                return 1
        i = i+1
    return 2

autentica('pedro', 'rie4co')
if autentica == 0:
    print("Autenticado com sucesso")
elif autentica == 1:
    print("Senha invalida")
elif autentica ==2:
    print("Tudo Errado")

            

