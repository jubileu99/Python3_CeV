# Algoritmo para calcular a hipotenusa de um triângulo.
import math
catA = float(input("Informe o cateto adjacente "))
catO = float(input("Informe o cateto oposto "))
# hipo = math.sqrt(math.pow(catA,2)+math.pow(catO,2))
hipo = math.hypot(catA,catO)
print("O valor da hipotenusa é {:.4f}".format(hipo))