from fastapi import FastAPI

app = FastAPI()

@app.get("/produtos")
def listar_produtos():
    return [
        {
            "nome": "Nutella",
            "preco": 25.00
        },
        {
            "nome": "Macarrão",
            "preco": 7.00
        }  
    ]