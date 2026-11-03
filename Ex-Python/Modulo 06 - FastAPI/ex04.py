from fastapi import FastAPI
from pydantic import BaseModel, Field

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

class Produto(BaseModel):
    nome: str = Field(min_length=1)
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