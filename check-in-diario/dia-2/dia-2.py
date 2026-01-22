# Programa para calcular a média de três notas e determinar a situação do aluno
def lernota(numero):   
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota: "))
            if nota >= 0 and nota <= 10:
                return nota
            else:
                print("Notas devem estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

nota1 = lernota(1)
nota2 = lernota(2)
nota3 = lernota(3)
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f"Aluno aprovado com média {media:.2f}")
elif media >= 4:
    print(f"Aluno em recuperação com média {media:.2f}")
else:
    print(f"Aluno reprovado com média {media:.2f}")
print("Fim do programa.")
