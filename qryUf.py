import time
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from selenium import webdriver

def finder(data_uf,url):
    req=requests.post(url,data_uf)
    content=req.content
    site=BeautifulSoup(content, 'html.parser')
    site.find('div', attrs={'class': 'column2'})










    
    '''driver=webdriver.Chrome('C:/Users/denni/OneDrive/Documentos/chromedriver_win32/chromedriver')
    driver.get(req)
    element=driver.find_element_by_xpath("//table[@class='tmptabela']//tbody//tr")
    html=element.get.attribute('outerHTML')
    print(html)


    time.sleep(3)
    driver.quit()'''












    '''values='UF='+data_uf+'&'+"Localidade="
    print(values)

    httpRequest= urllib2.Request(url,values)
    
    html = req.text
    

    dataRead= r"(?:<tr.*?>)(.*?)(?:</tr>)"
    result= re.findall(dataRead,html)

    print (result[0])
    print (result[1])'''
# -----------------------------------------------


url='http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
values={
    'UF':'SC',
    'Localidade':''
    }

finder(values,url) 