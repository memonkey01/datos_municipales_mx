# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:56:57 2020

@author: izqui
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url_path= 'http://codigo-postal.es.mapawi.com/'
driver = webdriver.Chrome()

cp_file = pd.read_csv('datos/mx_postal_codes.csv', encoding='latin1')
cp_file_main = cp_file['Postal Code'].unique()
cp_list = cp_file_main.astype(str).tolist()

cp_list2 = cp_list[9024:]

3417+1484+4123

cp_of_list = []
lat_list = []
lon_list = []

for cp in cp_list2:

  #  driver = webdriver.Chrome()
    driver.get(url_path)
    text_box = driver.find_element_by_name("search")
    text_box.send_keys(cp)
    try:
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/div[1]/div/form/select/option[8]").click()
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table/tbody/tr/td/div[1]/div/form/input[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td[1]/a").click()
        soup= BeautifulSoup(driver.page_source, 'lxml')
        html_screenshot = str(soup)
        latitud = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/font[7]").text
        longitud = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/font[9]").text
        cp_of_list.append(cp)
        lat_list.append(latitud)
        lon_list.append(longitud)
        print('CODIGO BUSCADO {}'.format(cp))
        time.sleep(2)
    except:
        latitud = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/font[7]").text
        longitud = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/div/table[2]/tbody/tr/td[2]/font[9]").text
        cp_of_list.append(cp)
        lat_list.append(latitud)
        lon_list.append(longitud)
        print('CODIGO BUSCADO {}'.format(cp))
        time.sleep(2)
        
        
temp_df = pd.DataFrame({'Postal Code':cp_of_list,'Latitude_ex':lat_list,'Longitude_ex':lon_list})
#temp_df.to_pickle('cp_3.pkl')
