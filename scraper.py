import requests
from bs4 import BeautifulSoup

url ='https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?tipoDocumento=Todos'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
normas = soup.find_all('div', class_='encontrados')
paginas = soup.find_all('li', class_='page-link')

norma = normas[0]
titulos = norma.find('a', class_='resultado item').get_text()


