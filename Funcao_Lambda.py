# Uso da função Lambda

# Método convencioanl
preco = 1000

def calcula_imposto(preco):
    return preco * 0.3
print("Imposto: {}".format (calcula_imposto(preco)))

# Usando Função Lambda
calcular_imposto2 = lambda x: x * 0.3
print("Imposto usando lambda: {}".format (calcular_imposto2(preco)))

# Função lambda em outra função - Cálculo imposto de 30% em cada preço da lista
precos = [125, 400, 15, 37]
impostos = list(map(lambda x: x*0.3, precos)) # 'list' só informa que será retornado uma lista. 'map' serve para mapear a função lambda em cada item da lista
print("Imposto com map e lambda: {}".format (impostos))