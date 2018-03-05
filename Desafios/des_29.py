velo = int(input("Insira a velocidade do carro: "))
if velo > 80:
    print("Você foi multado por ultrapssar os 80km/h e sua multa será de {} reais".format((velo-80)*7))
else:
    print("Pode seguir a viajem!")