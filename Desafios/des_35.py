r1 = float(input("Informe o valor da reta 1º "))
r2 = float(input("Informe o valor da reta 2º "))
r3 = float(input("Informe o valor da reta 3º "))

if r2-r3 < r1 < r2+r3 and r1-r3 < r2 < r1+r3 and r1-r2 < r3 < r1+r2:
    print("Pode-se formar triângulos com as retas {} {} {}".format(r1,r2,r3))
else:
    print("Infelizmente não será possivel formar um triângulo!")