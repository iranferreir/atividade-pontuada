import os 
os.system("cls || clear")

lista_nomes =[]

# Entrada.
print("=== Solicitando dados para o usuario ===")
while True:
    nome = input("Digite seu nome ")
    if nome.lower() == "sair":
        break
    else:
        lista_nomes.append(nome)

# Processamento.
print("\nOrdenando lista...")
lista_ordenada = sorted(lista_nomes)

# Saida
print("\n=== Resultado ===")
print("lista original:")
print(lista_nomes)

print("\nLista ordenando:")
print(lista_ordenada)