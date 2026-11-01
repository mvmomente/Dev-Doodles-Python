import json

with open("usuario.json", "r") as arquivo:
    usuario = json.load(arquivo)

    print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")