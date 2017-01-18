# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:05:46 2016

@author: Dylan
"""


from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import math
import re
import lxml.html
from lxml.cssselect import CSSSelector
import requests
import pandas as pd
import time
import datetime
import pyodbc
from itertools import chain
import re
import sys
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cellyoular.settings')
        
storage_dict = {1:8,2:16,3:32,4:64,8:128,9:256}
        
swappa =  'https://swappa.com/buy/iphones'


def populate():
    
    soup = BeautifulSoup(requests.get(swappa).text, 'lxml')
    links = ['https://swappa.com' + i.div.a['href'] for i in soup.findAll('div', { 'class':"col-md-3 col-sm-4 col-xs-4"})]
    for link in links:
        print('Trying ' + link) 
        
        s = BeautifulSoup(requests.get(link).text, 'lxml')
    
        page_links = ['https://swappa.com' + i.a['href'] for i in s.findAll('div', {'class': "col-md-3 col-xs-6"})]
    
        for page in page_links:
            print('Trying ' + page) 
            s1 = BeautifulSoup(requests.get(page).text, 'lxml')
            name = s1.findAll('section', {'id':'breadcrumbs'})[0].findAll('li')[2].a.text
            carrier = s1.findAll('section', {'id':'breadcrumbs'})[0].findAll('li')[3].a.text
            data = s1.findAll(True, {'class': ['listing_preview featured','listing_preview']})
            for d in data:
                print(d['data-code'], int(d['data-price']), d['data-condition'],d['data-date'], storage_dict[int(d['data-storage'])])
                #p = Phone(code=d['data-code'], name=name, carrier=carrier, price=int(d['data-price']),condition=d['data-condition'],date_listed=d['data-date'],storage=storage_dict[int(d['data-storage'])])
                Phone.objects.get_or_create(code=d['data-code'], name=name, carrier=carrier, price=int(d['data-price']), condition=d['data-condition'],date_listed=d['data-date'],storage= storage_dict[int(d['data-storage'])])
    
# Start execution
if __name__ == '__main__':
    print("Starting phone population script...")
    django.setup()
    from home.models import Phone
    populate()
                
            







