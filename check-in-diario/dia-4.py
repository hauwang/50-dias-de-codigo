def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ").strip()

    while True:
        try:
            nota = float(input("Nota do aluno (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

    alunos.append({
        "nome": nome,
        "nota": nota
    })
    print("Aluno cadastrado com sucesso!\n")


def mostrar_resultados(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    soma = 0
    aprovados = []
    reprovados = []

    for aluno in alunos:
        soma += aluno["nota"]
        if aluno["nota"] >= 7:
            aprovados.append(aluno["nome"])
        else:
            reprovados.append(aluno["nome"])

    media = soma / len(alunos)

    print("\n📊 RESULTADOS")
    print(f"Média da turma: {media:.2f}")

    print("\nAprovados:")
    for nome in aprovados:
        print(f"- {nome}")

    print("\nReprovados:")
    for nome in reprovados:
        print(f"- {nome}")
    print()


def menu():
    alunos = []

    while True:
        print("===== MENU =====")
        print("1 - Cadastrar aluno")
        print("2 - Mostrar resultados")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            mostrar_resultados(alunos)
        elif opcao == "3":
            print("Encerrando o sistema. Até mais! 👋")
            break
        else:
            print("Opção inválida.\n")


menu()