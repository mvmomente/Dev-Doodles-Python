import json
from util import criar_usuario, editar_usuario, excluir_usuario, carregar_usuarios, listar_usuarios

usuarios = listar_usuarios()

criar_usuario("Marcos", 27, True)
editar_usuario("Paulo", 27)
excluir_usuario("Roberto")

for usuario in usuarios:
    print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")

print("--------------------------------------------------------------")

for usuario in usuarios:
    if usuario["idade"] >= 30:
        print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")