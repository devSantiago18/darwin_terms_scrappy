""" comparar el historial de terminos con los terminos soportados actualmente y saber en que categoria se encuentran"""
history_tems = open('list_history.json', 'r').read()
categories_terms = open('categories.json', 'r').read()

import json
by_categories = json.loads(categories_terms)
by_history = json.loads(history_tems)

print(by_categories)
for name, attrs in by_history.items():
    term = name[4:] 
    for categorie, items in by_categories.items():
        if term in items:
            print(f'{term} is in {categorie} categorie')
    