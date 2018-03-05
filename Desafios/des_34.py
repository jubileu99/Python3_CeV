salario = float(input("Informe o seu salário: "))
if salario > 1250:
    print("O seu salário de {} sofrerá um aumento de 10% e passará a ser {}".format(salario,(salario*0.10)+salario))
else:
    print("O seu salário de {} sofrerá um aumento de 15% e passará a ser {}".format(salario, (salario * 0.15) + salario))