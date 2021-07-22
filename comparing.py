""" comparar el historial de terminos con los terminos soportados actualmente y saber en que categoria se encuentran"""
history_tems = open('list_history.json', 'r').read()
categories_terms = open('categories.json', 'r').read()

import json
term_categories = json.loads(categories_terms)
term_history = json.loads(history_tems)


def str_ult_name(name:str):
    index = name.index(':')
    return name[index+1:]


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
with open ('clasifications.json', 'w') as jsonFile:
    jsonFile.write(json_class)

"""
for categorie, items in term_categories.items():
    for term in terms:
        if term in items:
            dic_new_categories[categorie].append(term)
            flat_noone = False
        
"""
print(dic_new_categories)
#for categories, items in by_categories:
