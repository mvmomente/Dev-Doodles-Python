from fastapi import FastAPI, HTTPException

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

@app.get("/produtos/{nome}")
def buscar_produto(nome):
    for produto in produtos:
        if produto.get("nome") == nome:
            return produto
    
    else:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )