from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

produtos = [
    {
        "nome": "Nutella",
        "preco": 35.50
    },
    {
        "nome": "Teclado",
        "preco": 150.00
    }
]

class Produto(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        if not valor.strip():
            raise ValueError("O nome não pode estar vazio")

        return valor.strip()
    
class AtualizarPreco(BaseModel):
    preco: float = Field(gt=0)

@app.get("/")
def inicio():
    return{"mensagem": "Minha primeira API!"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{nome_produto}")
def visualizar_produto(nome_produto):
    for produto in produtos:
        if produto["nome"] == nome_produto:
            return produto

    else:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

@app.post("/produtos")
def cadastrar_produto(produto: Produto):
    produtos.append(
        {
            "nome": produto.nome,
            "preco": produto.preco
        }
    )

    return produto

@app.put("/produtos/{nome_produto}")
def atualizar_produto(nome_produto: str, novos_dados: Produto):

    for produto in produtos:
        if produto["nome"] == nome_produto:
            produto["nome"] = novos_dados.nome
            produto["preco"] = novos_dados.preco
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

@app.patch("/produtos/{nome_produto}")
def atualizar_preco(nome_produto: str, novos_dados: AtualizarPreco):

    for produto in produtos:
        if produto["nome"] == nome_produto:
            produto["preco"] = novos_dados.preco
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

@app.delete("/produtos/{nome_produto}")
def deletar_produto(nome_produto: str):
    for produto in produtos:
        if produto["nome"] == nome_produto:
            produtos.remove(produto)
            return ({"message": "Produto removido com sucesso"})
    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )