from fastapi import FastAPI
from pydantic import BaseModel

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
    nome: str
    preco: float

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