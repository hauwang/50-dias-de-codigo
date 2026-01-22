# Andrews Soares
# 19 de janeiro de 2026
# DESAFIO 1 - FUNDAMENTOS

from time import sleep

print('*-*' * 12)
print("Bem-vindo ao Desafio 1 - Fundamentos!")
print('*-*' * 12)
sleep(1)
print("Este programa solicitará três números inteiros, calculará a soma e a média deles e indentificará o maior e menor valor.\n")
sleep(2)

while True:
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        sleep(0.5)
        num2 = int(input("Digite o segundo número inteiro: "))
        sleep(0.5)
        num3 = int(input("Digite o terceiro número inteiro: "))
      
        soma = num1 + num2 + num3
        media = soma / 3

        print("\nCalculando os resultados...\n")

        sleep(2)
        print("-" * 30)
        print(f"A soma dos três números é: {soma}")
        print(f"A média dos três números é: {media:.1f}")
        print(f"O maior número é: {max(num1, num2, num3)}")
        print(f"O menor número é: {min(num1, num2, num3)}")
        print("-" * 30)
        sleep(1)

        dnv = input("\nDeseja realizar outra operação? 'S' para continuar ou tecla qualquer para encerrar: ").strip().lower()
        if dnv == 's':
           continue
        else:
            print('OBRIGADO POR USAR O PROGRAMA')
            break

    except ValueError:
        print("ERRO! Por favor, insira apenas números inteiros.")
        sleep(1)
        continue
