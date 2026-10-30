nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Olá {nome}! Você é maior de idade")
else:
    print(f"Olá {nome}! Você é menor de idade")