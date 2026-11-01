import json

usuario = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "São Paulo"
}

dados = json.dumps(usuario)

print(dados)