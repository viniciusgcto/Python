import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%*()-=+,.;:/?'

rnd = random.SystemRandom() # Utiliza a classe 'urandom' da biblioteca 'OS'

print(''.join(rnd.choice(chars) for i in range (tamanho)))
