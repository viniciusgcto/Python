import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

#a = float(input("Digite A: ")) #Para usar o INPUT e o usuário fornecer o dado
#b = float(input("Digite B: ")) #Para usar o INPUT e o usuário fornecer o dado


p1 = float(3.5)
p2 = float(7.5)
#TODO: Complete os espaços em branco com as respectivas variáveis para o cálculo da média.
media = ((p1*a) + (p2*b)) / (p1+p2)

#TODO: Complete com a variável que representa o resultado da média.
print(f'MEDIA ={media : .5f}')

