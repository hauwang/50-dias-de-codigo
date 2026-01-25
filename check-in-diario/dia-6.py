pessoas = []

while True:
    nome = input("Nome da pessoa (ou 'sair' para encerrar): ").strip()

    if nome.lower() == "sair":
        break

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        continue

    try:
        salario = float(input("Salário: "))
    except ValueError:
        print("Salário inválido.")
        continue

    pessoas.append({
        "nome": nome,
        "idade": idade,
        "salario": salario
    })

if len(pessoas) == 0:
    print("Nenhum cadastro realizado.")
else:
    total = len(pessoas)
    soma_salarios = 0
    maiores_idade = 0
    maior_salario = pessoas[0]["salario"]
    nome_maior_salario = pessoas[0]["nome"]

    for p in pessoas:
        soma_salarios += p["salario"]

        if p["idade"] >= 18:
            maiores_idade += 1

        if p["salario"] > maior_salario:
            maior_salario = p["salario"]
            nome_maior_salario = p["nome"]

    media_salarial = soma_salarios / total

    print("\n📊 RELATÓRIO FINAL")
    print(f"Total de pessoas cadastradas: {total}")
    print(f"Maiores de idade: {maiores_idade}")
    print(f"Média salarial: R$ {media_salarial:.2f}")
    print(f"Maior salário: R$ {maior_salario:.2f} ({nome_maior_salario})")