#Função retorna um valor, método não. O Def no Python, retornando valor é uma função

def soma (a, b) :
    return a + b
if (__name__ == '__main__'):
    print(soma(1,2))

#Exemplo de classe como método (sem returnar "return" valor)
# __init__ serve para inicializar uma funcao

class Televisao:
        def __init__(self):
            self.ligada = False
        
        def power(self):
            if self.ligada :
                self.ligada = False
            else :
                self.ligada = True


if (__name__ == '__main__'):
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)