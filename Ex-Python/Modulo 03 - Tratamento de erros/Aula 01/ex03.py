try:
    age = int(input("Digite sua idade: "))

except ValueError:
    print("Digite um número inteiro!")

else:
    print(f"Idade registrada {age}")

finally:
    print("Programa finalizado!")