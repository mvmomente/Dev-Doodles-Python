userName = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
auth = input("Você tem autorização? (sim/não): ").lower()

if age >= 18 and auth == "sim":
    print(f"Olá {userName}, você é maior de idade.")
else:
    print(f"Olá {userName}, você é menor de idade.")