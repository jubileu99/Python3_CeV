dias = int(input("Informe o número de dias "))
km = float(input("Informe o número de km's "))
calc = (dias*60) + (km*0.15)
print("###Dias = {}\n###Km's = {} \n###Total a pagar = R$ {:.2f} ".format(dias,km,calc))