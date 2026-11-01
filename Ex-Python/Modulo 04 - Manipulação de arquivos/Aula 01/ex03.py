with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())