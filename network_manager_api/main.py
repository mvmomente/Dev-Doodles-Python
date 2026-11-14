from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

vpcs = []

def buscar_vpc(nome):
    for vpc in vpcs:
        if vpc["nome"] == nome:
            return vpc
        
    return None

class VPC(BaseModel):
    nome: str
    cidr: str
    regiao: str

class VPCAtualizacao(BaseModel):
    nome: str | None = None
    cidr: str | None = None
    regiao: str | None = None

@app.get("/")
def homepage():
    return "Network Manager API"

@app.get("/vpcs")
def listar_vpcs():
    return vpcs

@app.get("/vpcs/{nome}")
def consultar_vpc(nome: str):
    resultado = buscar_vpc(nome)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="VPC não encontrada"
        )

    return resultado

@app.post("/vpcs", status_code=201)
def criar_vpc(nova_vpc : VPC):

    for vpc in vpcs:
        if vpc["nome"] == nova_vpc.nome:
            raise HTTPException(
                status_code=409,
                detail="Ja existe uma VPC com esse nome"
            )
        
    vpcs.append(nova_vpc.model_dump())
    return nova_vpc


@app.patch("/vpcs/{nome}", status_code=200)
def atualizar_vpc(nome: str, atualizacao: VPCAtualizacao):
    dados = atualizacao.model_dump(exclude_unset=True)
    vpc_encontrada = None

    for vpc in vpcs:
        if vpc["nome"] == nome:
            vpc_encontrada = vpc
            break

    if vpc_encontrada is None:
        raise HTTPException(
            status_code=404,
            detail="VPC não encontrada"
        )

    if "nome" in dados:
        novo_nome = dados["nome"]

        for outra_vpc in vpcs:
            if outra_vpc["nome"] == novo_nome and outra_vpc is not vpc_encontrada:
                raise HTTPException(
                    status_code=409,
                    detail="Ja existe uma VPC com esse nome"
                )

    vpc_encontrada.update(dados)
    return vpc_encontrada