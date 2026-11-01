import json

dados = '{"nome": "Marcos", "idade": 26, "ativo": true}'

usuario = json.loads(dados)

print(f"Nome: {usuario["nome"]}")

if usuario["ativo"]:
    print("Usuario autorizado")
else:
    print("Usuario inativo")