import random
print("#################################################################################")
print("Jogo da adivinhação :))")
print("O Computador irá gerar um número de 1 a 5 e você terá que adivinhar este número, boa sorte !")
num = int(input("Informe um número de 1 a 5 "))
pc = random.randint(1,5)

if num >= 1 and num <=5:
    if num == pc:
        print("Acertou mizeravi")
    else:
        print("Tente novamente!")
else:
    print("Número inválido!")
