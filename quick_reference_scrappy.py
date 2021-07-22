from os import terminal_size
from bs4 import BeautifulSoup
from get_data import get_data_html
import json

_, quick_reference_html = get_data_html()

class_names = []
terms = []
soup = BeautifulSoup(quick_reference_html, 'html.parser')

h2_ = soup.find_all('h2')
divs_ = soup.find_all('div', class_='my-4')
#print(len(divs_), len(h2_))

for h2 in h2_:
    class_names.append(h2.text)

for div in divs_:
    terms_aux = []
    for element in div:
        if element.string in ['\n',  ['\n']]:
            continue
        else:
            terms_aux.append(element.string)
    if len(terms_aux) > 0: terms.append(terms_aux)


dic_class = dict(zip(class_names, terms))

json_class = json.dumps(dic_class)
with open ('categories.json', 'w') as jsonFile:
    jsonFile.write(json_class)



print(len(dic_class))
