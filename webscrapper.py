from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.uai.com.br/").content
# 'site' recebe todo conteúdo da requisição http do site

soup = BeautifulSoup(site, 'html.parser')
# soup baixa do site o html

##print(soup.prettify())
# transforma o html em string e o print vai exibir todo código html

print(soup.title.string)
# Imprime o título do site

##noticia = soup.find('span', class_= "news -title")
noticia = soup.find('span', {'class' : 'news -title'})
# armazena a classe de uma tag 'span' no site para, neste caso, a manchete

print(noticia.string)
# imprime a manchete do site
