while True:
    sequencia = (int(input("Digite a sequencia: ")))
    c = 0
    while c <1:
        soma = sequencia + 1
        potencia = soma ** 2
        codigo = potencia - 1
        print ("O Codigo é: {} ".format(codigo))
        c += 1
        input ("Aperte enter para continuar!")
