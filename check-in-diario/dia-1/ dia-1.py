#Cadastro com validação
print('**'*11)
print('BEM VINDO AO CADASTRO')
print('**'*11)
while True:
    try:
        nome = str(input('SEU NOME: ')).upper()
        idade = int(input('SUA IDADE: '))
        salario = float(input('SEU SALÁRIO: R$'))
        if nome == '' or idade < 0 or salario < 0:
            print('Por favor, preencha todos os campos corretamente.')
            continue
        else:
            print('**'*11)
            print(f'CADASTRO REALIZADO COM SUCESSO!\nNOME: {nome}\nIDADE: {idade} anos\nSALÁRIO: R${salario:.2f}')
            print('**'*11)
            dnv = str(input('DESEJA FAZER OUTRO CADASTRO? [S/N]: ')).upper().strip()[0]
            if dnv == 'S':
                continue
            elif dnv == 'N':
                print('ENCERRANDO O CADASTRO. ATÉ MAIS!')
                break
            else:
                print('Opção inválida. Encerrando o cadastro.')
                break
    except ValueError:
        print('Por favor, insira um número válido para a idade.')
        continue
      
