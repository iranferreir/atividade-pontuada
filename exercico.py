"""
Dada uma lista de palavras, escrava um porgrama que solicite ao usuario uma lista de frutas e mostre:
- a lista original
- a lista ordenada
- a lista na ordem inversa

Caso o usuario digite sair, pare de solicitar dados. 

REFATORANDO CODIGO:
Crie uma funcao para:
    - Ordenacao
    - Ordenacao na ordem inversa
"""

import os 
os.system("cls || clear")

lista_de_frutas = []

def ordenar_lista(lista):
    """
    Função que ordena a lista de frutas em ordem crescente.
    """
    return sorted(lista)

def ordenar_invertido(lista):
    """
    Função que ordena a lista de frutas em ordem decrescente.
    """
    return sorted(lista, reverse=True)

def main():
    frutas = []
    
    while True:
        fruta = input("Digite uma fruta (ou 'sair' para encerrar): ").strip()
        
        if fruta.lower() == 'sair':
            break
        
        frutas.append(fruta)
    
    # Exibe a lista original
    print("\nLista original:")
    print(frutas)
    
    # Exibe a lista ordenada
    lista_ordenada = ordenar_lista(frutas)
    print("\nLista ordenada:")
    print(lista_ordenada)
    
    # Exibe a lista ordenada na ordem inversa
    lista_invertida = ordenar_invertido(frutas)
    print("\nLista ordenada na ordem inversa:")
    print(lista_invertida)

if __name__ == "__main__":
    main()
