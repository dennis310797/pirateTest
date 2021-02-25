import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:/Users/denni/OneDrive/Documentos/chromedriver_win32/chromedriver')
driver.get('https://www.4devs.com.br/gerador_de_numeros_aleatorios')
time.sleep(1)
#search_box = driver.find_element_by_xpath("//div[@class='card card--xl medium-4 columns']//a[@href='/gerador_de_cpf']").click()
search_box = driver.find_element_by_xpath("//div[@id='area_resposta']//tbody")
html=search_box.get_attribute('outerHTML')

soup=BeautifulSoup(html,'html.parser')
table=soup.find(name='tbody')

#df_full=pd.read_html(str(table))[0].head(5)
print(type(table))

time.sleep(1)
driver.quit() 
