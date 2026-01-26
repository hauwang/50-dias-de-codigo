estoque = []

while True:
    produto = input("Nome do produto (ou 'sair' para encerrar): ").strip()

    if produto.lower() == "sair":
        break

    try:
        quantidade = int(input("Quantidade em estoque: "))
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
            continue
    except ValueError:
        print("Digite um número inteiro para a quantidade.")
        continue

    try:
        preco = float(input("Preço do produto: "))
        if preco <= 0:
            print("O preço deve ser maior que zero.")
            continue
    except ValueError:
        print("Digite um valor numérico para o preço.")
        continue

    estoque.append({
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco
    })

if len(estoque) == 0:
    print("Nenhum produto cadastrado.")
else:
    total_itens = 0
    valor_total = 0
    maior_valor = estoque[0]["preco"] * estoque[0]["quantidade"]
    produto_mais_caro = estoque[0]["produto"]

    for item in estoque:
        total_itens += item["quantidade"]
        valor_item = item["quantidade"] * item["preco"]
        valor_total += valor_item

        if valor_item > maior_valor:
            maior_valor = valor_item
            produto_mais_caro = item["produto"]

    print("\n📦 RELATÓRIO DE ESTOQUE")
    print(f"Total de itens em estoque: {total_itens}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")
    print(f"Produto com maior valor em estoque: {produto_mais_caro}")