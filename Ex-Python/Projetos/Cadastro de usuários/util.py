import json

# CARREGAR USUARIOS
def carregar_usuarios():
    with open("usuarios.json", "r") as arquivo:
        return json.load(arquivo)

# SALVAR USUARIOS
def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)
# LISTAR USUARIOS
def listar_usuarios():
    usuarios_salvo = carregar_usuarios()
    return usuarios_salvo

# CRIAR
def criar_usuario(nome, idade, ativo):
    usuarios_salvo = carregar_usuarios()
    usuario_existe = any(usuario["nome"] == nome for usuario in usuarios_salvo)

    if usuario_existe:
        print("Usuario ja cadastrado")
    else:
        novo_usuario = {
            "nome": nome,
            "idade": idade,
            "ativo": ativo
        }
        usuarios_salvo.append(novo_usuario)
        salvar_usuarios(usuarios_salvo)


# EDITAR
def editar_usuario(nome, idade):
    usuarios_salvo = carregar_usuarios()
    for usuario in usuarios_salvo:
        if usuario["nome"] == nome:
            usuario["idade"] = idade

            salvar_usuarios(usuarios_salvo)
            break
    else:
        print("Usuario não encontrado")

# EXCLUIR
def excluir_usuario(nome):
    usuarios_salvo = carregar_usuarios()
    for usuario in usuarios_salvo:
        if usuario["nome"] == nome:
            usuarios_salvo.remove(usuario)
            salvar_usuarios(usuarios_salvo)
            break
    else:
        print("Usuario não encontrado")
