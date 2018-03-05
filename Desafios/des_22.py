frase = str(input("Informe o seu nome: "))
print("Nome em upperCase:",frase.upper()) # Todas a letras maiusculas
print("Nome em lowerCase:",frase.lower()) # Todas as letras minusculas
frase = frase.split()
print("O primeiro nome tem:",len(frase[0]),"Caracteres")
frase = ''.join(frase)
print("Nº de caracteres sem espaço: ",len(frase))