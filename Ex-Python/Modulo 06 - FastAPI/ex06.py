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

class Produto(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        if not valor.strip():
            raise ValueError("O nome não pode estar vazio")
        return valor.strip()

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

@app.put("/produtos/{produto_nome}")
def atualizar_produto(produto_nome: str, novo_produto: Produto):
    
    for produto in produtos:
        if produto["nome"] == produto_nome:
            produto["preco"] = novo_produto.preco

            return produto

        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )