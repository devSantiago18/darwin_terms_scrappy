"""
    this module performs scrapping to extract the classes from the darwin core terms
"""
history_tems = open('./resources/json/list_history.json', 'r').read()
categories_terms = open('./resources/json/categories.json', 'r').read()

import json
term_categories = json.loads(categories_terms)
term_history = json.loads(history_tems)


def str_ult_name(name:str):
    index = name.index(':') + 1
    return name[index:]


terms = term_history.keys()
terms = list(map(str_ult_name, terms))

dic_new_categories = { x : [] for x in term_categories.keys()}
dic_new_categories['Deprecated'] = []

#print(by_categories)

for term in terms:
    flat_any = True
    for categories in term_categories.keys():
        if term in term_categories[categories]:
            dic_new_categories[categories].append(term)
            flat_any = False
    if flat_any:
        dic_new_categories['Deprecated'].append(term)
    
for key, value in dic_new_categories.items():
    dic_new_categories[key] = list(dict.fromkeys(value))

json_class = json.dumps(dic_new_categories)
with open ('./resources/json/clasifications.json', 'w') as jsonFile:
    jsonFile.write(json_class)

