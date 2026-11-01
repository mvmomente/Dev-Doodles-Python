nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <= 0:
    print(f"Olá {nome}! Digite uma idade válida")
elif idade <= 12:
    print(f"Olá {nome}! Você é uma criança")
elif idade <= 17:
    print(f"Olá {nome}! Você é um adolescente")
elif idade <= 59:
    print(f"Olá {nome}! Você é um adulto")
else:
    print(f"Olá {nome}! Você é um idoso")