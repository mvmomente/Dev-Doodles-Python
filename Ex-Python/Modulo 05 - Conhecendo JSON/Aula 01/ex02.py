import json

dados = '{"nome": "Carlos", "idade": 30, "cidade": "Campinas"}'

usuario = json.loads(dados)

print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")