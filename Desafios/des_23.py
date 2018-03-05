numero = int(input("Informe um número de 0 até 9999: "))


# Faz a divisão inteira do número e pega o resto da divisão por 10.

u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10

print("Milhar:{}".format(m))
print("Centeza:{}".format(c))
print("Dezena:{}".format(d))
print("Unidade:{}".format(u))





