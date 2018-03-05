import random
print("Insira o nome dos alunos")
name1 = str(input())
name2 = str(input())
name3 = str(input())
name4 = str(input())

sorteado = random.choice([name1,name2,name3,name4])
print("O aluno sorteado é: {}".format(sorteado))


