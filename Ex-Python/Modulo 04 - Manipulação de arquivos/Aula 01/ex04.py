with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:

        nome = linha.strip()

        if len(nome) > 4:
            print(nome)