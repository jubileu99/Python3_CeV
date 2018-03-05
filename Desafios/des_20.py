from random import shuffle
print("Insira o nome dos alunos") # Escreve na tela
n1 = str(input()) #
n2 = str(input()) #
n3 = str(input()) #
n4 = str(input()) #
lista = [n1,n2,n3,n4] # Cria uma lista com os elementos n
shuffle(lista) # Mistura os elementos da lista
# print("A ordem de apresentação será:\n{}".format(lista))
print("1º - {}\n2º - {}\n3º - {}\n4º - {}".format(lista[0],lista[1],lista[2],lista[3])) # Mostra a ordem de sorteio


