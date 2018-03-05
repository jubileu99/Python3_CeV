frase = "Curso de python do Gustavo Guanabara"
print(frase[0:2:2])
print(len(frase)) # Informar quantos caracteres a string possui
print(frase.count("o",0,15)) # Busca a letra 'o' na frase entre os caracteres 0 há 14 (pois vai até o 15 mais ele não irá ser contado)
print(frase.find("py")) # ira retornar a posicao inicial da palavra, no caso 9.
print(frase.find("gg")) # Ira retornar -1 pois a posição da palavra GG nao existe na frase.
print(frase.replace("Curso","Java")) # Substituir palavras
print(frase.upper()) # muda as palavras para UpperCase
print(frase.lower()) # Muda as palavras para LowerCase
print(frase.capitalize()) # muda todas as letras para LowerCase e deixa a primeira com UpperCase
print(frase.title()) # Todas as palavras ficam a com letras UpperCase (primeira)
frase.strip() # Tira os espaços das extremidades
frase.lstrip() # Tira os espaços na extremidade da esquerda
frase.rstrip() # Tira os espaços na extremidade da direita
frase = frase.split() # Pesquisa - Faz a divasão de palavras por meio dos espaços e atribui a variavel frase o split dado
print('-'.join(frase)) # Junta as palavras com o ' - ' no lugar dos espaços
print('Curso' in frase) # verifica se a palavra 'Curso' está na string frase, retorna True ou False
print(frase[2][4]) # Pega a 3 palavra da lista (python) e depois pega a 5 letra da frase





print("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet consectetur nulla, eu posuere urna hendrerit et.
Sed ut lobortis eros. Proin tristique commodo laoreet. Vivamus mollis commodo ipsum, id mattis tellus tempor non. Nunc at or
""")
