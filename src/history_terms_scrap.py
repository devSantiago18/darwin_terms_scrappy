"""
    this module scrapes in the document collected by 'get_data.py' to create a json
    that contains all the terms of the Darwin Core standard exposed in your web
"""
import requests
from bs4 import BeautifulSoup
from get_data import get_data_html
import json

terms_history_html, quick_reference_html = get_data_html(True)

soup = BeautifulSoup(terms_history_html, 'html.parser')
names_terms = []

theads = soup.find_all('thead')
for x in theads:
    names_terms.append(x.text.strip()[11:]) # podria refactorizar esto con una expresion regular, pero aja
names_terms.pop(0) # para quitar la primera tabla que es la descripcion de los namespaces

tbodys = soup.find_all("tbody")
td_list = []
for x in tbodys:
    td = x.find_all('td')
    td_list.append(td)

td_list.pop(0)# para quitar la primera tabla que es la descripcion de los namespaces


FLAT = True
d = [] 
attrs = set()
for td in td_list:
    keys = []
    values = []
    for elem in td:
        if FLAT:
            if elem.text == '':
                keys.append('Deprecated')
                attrs.add("Deprecated")
                #count +=  # si funciona
            else:
                keys.append(elem.text)
                attrs.add(elem.text)
        else:
            values.append(elem.text)
        FLAT = not FLAT
    d.append(dict(zip(keys, values)))
    
dict_terms_history = dict(zip(names_terms, d))



def save_json(name, data):
    with open (f'./resources/json/{name}.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data))

save_json('list_history', dict_terms_history)
save_json('atributos', sorted(list(attrs), reverse=True))

