email = input("Digite seu email: ")
senha = bool(input("Digite sua senha: "))
tem_token = False

if senha or tem_token:
    print(f"Olá {email}, você está logado.")
else:
    print(f"Olá {email}, você não está logado.")