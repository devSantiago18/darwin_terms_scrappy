import requests
from bs4 import BeautifulSoup
from get_data import get_data_html
import json

terms_history_html, quick_reference_html = get_data_html(True)

soup = BeautifulSoup(terms_history_html, 'html.parser')
names_terms = []

theads = soup.find_all('thead')
for x in theads:
    names_terms.append(x.text.strip()[11:])
names_terms.pop(0) # para quitar la primera tabla que es la descripcion de los namespaces

tbodys = soup.find_all("tbody")
td_list = []
for x in tbodys:
    td = x.find_all('td')
    td_list.append(td)

td_list.pop(0)# para quitar la primera tabla que es la descripcion de los namespaces


keys = []
values = []
prop_terms = []
FLAT = True
for td in td_list:
    for index in range(len(td)):
        if FLAT:
            if td[index].text == "":
                keys.append("deprecated")
            else:
                keys.append(td[index].text)
            FLAT = not FLAT
        else:
            values.append(td[index].text)
            FLAT = not FLAT
    prop_terms.append(dict(zip(keys,values)))
    

to_json_data = { names_terms[x] : prop_terms[x] for x in range(len(names_terms)) }
print(len(to_json_data.keys()))


#js = json.dumps(dict(zip(names_terms, obj)))
js = json.dumps(to_json_data)

"""
#json_data = json.loads(js)
#print(len(json_data))
"""