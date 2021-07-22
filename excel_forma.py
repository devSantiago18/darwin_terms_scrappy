from os import name
from openpyxl import Workbook
import json

categories = json.loads(open('categories.json', 'r').read())
atributos = list(json.loads(open('atributos.json', 'r').read()))
clasifications = json.loads(open('clasifications.json', 'r').read())
history_tems = json.loads(open('list_history.json', 'r').read())


deprecated = atributos.pop(2)
list_colums = ["darwin core terms","Section", deprecated, *atributos]
print(list_colums, type(list_colums))

wb = Workbook()
hoja = wb.active
# Crea la fila del encabezado con los títulos
hoja.append(list_colums)


def get_setcion(name):
    index = name.index(':')
    name = name[index+1:]
    categories_current = []
    for category, items in categories.items():
        if name in items:
            categories_current.append(category)
    if categories_current == []: return "no section"
    return "/".join(categories_current)


for name_term, attrs_term in history_tems.items():
    aux_term = []
    for name_attr, attr in attrs_term.items():
        for x in list_colums:
            if x ==  "darwin core terms" :
                aux_term.append(name_term)
            elif x == "Section":
                aux_term.append(get_setcion(name_term))
            elif x in attrs_term:
                aux_term.append(attrs_term[x])
            else:
                aux_term.append(" ")
    hoja.append(aux_term)


wb.save('./build/data2.xlsx')
