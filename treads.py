import time
from threading import Thread
from traceback import TracebackException

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} KM: {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target=carro, args=[10,'Dendi'])
t_carro2 = Thread(target=carro, args=[20,'Vinicius'])

t_carro1.start()
t_carro2.start()
