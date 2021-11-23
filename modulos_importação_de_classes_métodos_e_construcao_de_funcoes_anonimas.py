#Lidando com módulos, importação de classes, métodos e construção de funções anônimas (lambda)

#importando a classe de outro arquivo Python
#importante: if (__name__ == '__main__'): no arquivo origem só vai rodar quando a chamada for no próprio arquivo
#importante: chamada de arquivos externos usando o 'import' não executam o conteúdo dentro do if (__name__ == '__main__'):

from metodo_definicao_funcao_Televisao import Televisao

televisao = Televisao()
print(televisao.ligada)