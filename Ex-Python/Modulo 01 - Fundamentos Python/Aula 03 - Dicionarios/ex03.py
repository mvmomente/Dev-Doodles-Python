users = [
    {"name": "Carlos", "age": 26},
    {"name": "Ana", "age": 16},
    {"name": "Marcos", "age": 13},
    {"name": "Vitor", "age": 18},
    {"name": "Jenifer", "age": 30}
]

for user in users:
    print(f"Nome: {user['name']} | Idade: {user['age']}")

for user in users:
    if user["age"] >= 18:
        print(f"Nome: {user["name"]} | Idade: {user["age"]}")