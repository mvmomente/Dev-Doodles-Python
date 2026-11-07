from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

produtos = [
    {
        "nome": "Nutella",
        "preco": 25.00
    },
    {
        "nome": "Macarrão",
        "preco": 7.00
    }
]

class AtualizarPreco(BaseModel):
    preco: float = Field(gt=0)

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.post("/produtos")
def cadastrar_produto(produto: Produto):
    produtos.append(
        {
            "nome": produto.nome,
            "preco": produto.preco
        }
    )

    return produto

@app.patch("/produtos/{produto_nome}")
def atualizar_preco(produto_nome: str, novos_dados: AtualizarPreco):

    for produto in produtos:
        if produto["nome"] == produto_nome:
            produto["preco"] = novos_dados.preco
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )