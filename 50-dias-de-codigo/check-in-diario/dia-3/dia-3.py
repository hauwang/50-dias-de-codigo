
from time import sleep

print("Bem-vindo ao Dia 3 do Check-in Diário!")
print("Hoje vamos praticar a manipulação de strings em Python.\n")
nome = input("Por favor, insira seu nome completo: ").strip()
print("\nAnalisando seu nome...\n")
sleep(1)
print(f"Seu nome em maiúsculas: {nome.upper()}")
print(f"Seu nome em minúsculas: {nome.lower()}")
print(f"Número total de caracteres (sem espaços): {len(nome.replace(' ', ''))}")
print(f"Número de caracteres no primeiro nome: {len(nome.split()[0])}")