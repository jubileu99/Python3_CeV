n1 = str(input('Escreva o seu nome: '))
print('Bem vindo {:_^20}!'.format(n1)) # deixa o nome no meio dos 20 espaços e faz _ (underline) nos espaços vazios.
print('Welcome {:<20}!'.format(n1)) # deixa a variavel em primeiro lugar dos 20 espaços
print('Saludos {:>20}!'.format(n1)) # deixa a variavel em ultimo lugar dos 20 espaços
print('Welcome {:=<20}'.format(n1)) # coloca o sinal de = (igual) nos espaços vazios.