nome = str(input("Informe o seu nome completo:"))
nome = nome.split()
print("Seja bem vindo {0} {1}.".format(nome[0],nome[len(nome)-1]))