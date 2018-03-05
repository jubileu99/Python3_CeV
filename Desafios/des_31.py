km = float(input("Informe a kilometragem da viajem: "))
if km > 200:
    print("Você irá pagar {:.2f} pela viajem de {}km's".format(km*0.45,km))
else:
    print("Você irá pagar {:.2f} pela viajem de {}km's".format(km*0.50,km))