numeros = []

while True:
    try:
        n = int(input("Digite um número inteiro (0 para sair): "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    if n == 0:
        break

    numeros.append(n)

if len(numeros) == 0:
    print("Nenhum número foi digitado.")
else:
    pares = 0
    impares = 0
    soma_positivos = 0
    negativos = []

    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

        if num > 0:
            soma_positivos += num
        elif num < 0:
            negativos.append(num)

    media_negativos = (
        sum(negativos) / len(negativos)
        if len(negativos) > 0 else 0
    )

    # remover repetidos mantendo a ordem
    sem_repeticao = []
    for num in numeros:
        if num not in sem_repeticao:
            sem_repeticao.append(num)

    print("\n📊 RELATÓRIO FINAL")
    print(f"Total de números: {len(numeros)}")
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    print(f"Soma dos positivos: {soma_positivos}")
    print(f"Média dos negativos: {media_negativos:.2f}")
    print(f"Maior número: {max(numeros)}")
    print(f"Menor número: {min(numeros)}")
    print(f"Números sem repetição: {sem_repeticao}")