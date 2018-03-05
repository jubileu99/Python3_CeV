ano = int(input("Informe um ano "))
calc1 = ano % 4 # tem que ser multiplo de 4
calc2 = ano % 400 # tem que ser multiplo de 400
calc3 = ano % 100 # Não pode ser multiplo de 100


if calc1 == 0 and calc3 != 0:
    print("O ano de {0} é bissexto".format(ano))
elif calc3 == 0:
    print("O ano de {0} é bissexto²".format(ano))
else:
    print("O ano de {} é normal".format(ano))