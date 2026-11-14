import ipaddress

try:
    rede = ipaddress.ip_network(input("Digite o IP: "))
    ip_utilizaveis = rede.num_addresses - 2

    print(f"Rede: {rede}")
    print(f"Endereços totais: {rede.num_addresses}")
    print(f"IPs utilizáveis: {ip_utilizaveis}")

except ValueError:
    print("CIDR inválido")