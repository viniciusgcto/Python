import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

# vai contas e imprimir as palavras mais utilizadas em determinada URL

def start(url):
    wordlist = [] # lista inicializa vazia
    source_code = requests.get(url).text # codigo fonte da URL
    soup = BeautifulSoup(source_code, 'html.parser') # passando somente o html

    for each_text in soup.findAll('div', {'class': 'entry-content'}):  # percorrendo conteúdo no site baseado na div e classe específica dentro do html
        content = each_text.text  # armazenando conteúdo como texto

        words = content.lower().split() # convertendo para minusculo e quebrando em palavras todo texto

        for each_word in words:  # percorrer cada palavra armazenada na variavel de palavras - words
            wordlist.append(each_word)  # lista de palavras vai ser preenchida com cada palavra
        clean_wordlist(wordlist)  # chama a função de limpar a lista de palavras

def clean_wordlist(wordlist):  # função de limpar lista de palavras
    clean_list = []  # recebe uma lista vazia que será usada para receber as palavras limpas - sem símbolos
    for word in wordlist:  # percorre palavra por palavra da lista de palavras
        symbols = '!@#$%^&(){[]}/;:<>"?.,'  # armazena esses símbolos em symbols

        for i in range(0, len(symbols)):  # percorre de 0 até o tamanho da variável symbols para comparar se existem símbolos nas palavras
            word = word.replace(symbols[i], '')  # cada palavra vai receber a própria palavra substituindo os símbolos (caso exista) por vazio
        
        if len(word) > 0:  # se tamanho da palavra for maior que 0, a lista de palavras limpas receberá a palavra sem símbolos
            clean_list.append(word)
    create_dictionary(clean_list)  # chama a função de criar dicionário passando a lista de palavras tratadas

def create_dictionary(clean_list):
    word_count = {}
    for word in clean_list:  # para cada palavra na lista de palavras limpas, vai contabilizar a incidência de cada palavra e incrementar o contador
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):  # percorre o contador de palavra exibindo a palavra e o número de ocorrências
        print(" % s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(15)  # guarda os 15 registros de maior incidência
    print(top)    


if __name__ == '__main__':  # chamada do próprio programa
    #start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
    start("https://blog.task.com.br/webmail-seguro/")  # coleta da URL e inicialização da função start