from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def codigo_nfe(url):
    #1- USANDO O SELENIUM PARA FAZER O REQUEST
    page = webdriver.Chrome('.\chromedriver.exe')
    page.get(url)

    #2- RECEBENDO O HTML
    soup=BeautifulSoup(page.page_source,'html.parser')
    
    #3- SELECIONANDO A TAG TBODY E PROCURANDO NA TABELA TODOS ELEMENTOS DA TAG 'TR'
    table = soup.find(name='tbody').find_all(name='tr')

    #4- USANDO A BIBLIOTECA PANDAS PARA LER O HTML DA TABELA
    df_full=pd.read_html(str(soup))[0].head(len(table))

    #5- APRESENTANDO A TABELA
    print(df_full)
    print("\n*********************************************")
    print(f"Selecionando um elemento da tabela: {df_full.UF[21:22]}")
    print("*********************************************")


    page.quit()
if __name__ == '__main__':
    url='https://www.oobj.com.br/bc/article/quais-os-c%C3%B3digos-de-cada-uf-no-brasil-465.html'
    codigo_nfe(url)