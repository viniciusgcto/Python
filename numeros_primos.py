num = int(input("Escreva um numero: "))
div = 0
for cont in range(1,num+1) :
    resto = num % cont
    if (resto == 0) :
        div += 1
if (div == 2) :
    print("O numero " + str(num) + " é primo")
else :
    print("O numero " + str(num) + " não é primo")
