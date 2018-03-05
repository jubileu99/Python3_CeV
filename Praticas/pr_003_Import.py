import math,random,emoji # Importa as bibliotecas math,random e emoji
num = random.random() # Gera um nº aleatoria de 0 a 1
num = num * 100 # Converte o nº de 0 a 1 para dezenas
num = math.ceil(num) # Arredonda o resultado para cima.
raiz = math.sqrt(num) # Calcula a raiz quadrada SQUARE ROOT
quadrado = math.pow(num,2) # Calcula a potência de 2, num²
print("A raiz do número random {0} é {1} \nO quadrado é {2}".format(num,raiz,quadrado)) # Mostra os resultados na tela
print(emoji.emojize("É tudo por hj pessoal :smirk: ", use_aliases=True)) #Adiciona um emoji

#
# print("A raiz do número random",num,"é igual a",raiz,"\nO quadrado é",quadrado)
#