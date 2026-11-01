import json

usuario = {
    "nome": "Ana",
    "idade": 28,
    "ativo": True
}

with open("usuario.json", "w") as arquivo:
    json.dump(usuario, arquivo)