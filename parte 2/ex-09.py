nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print(f"A nota {nota} é suficiente para aprovação.")
elif nota >= 4:
    print(f"A nota {nota} é insuficiente para aprovação, mas o aluno está de recuperação.")
else:
    print(f"A nota {nota} é insuficiente para aprovação e o aluno está reprovado.")