automovil={'Chevrolet':'Camaro','Color Auto':'Plomo','Tipo de Licencia':'D', 'Millas por galon':'520','millas':'500'}
book ={'tittle': 'Sunrise News', 'author':'Bob','year':2010}
software={'tittle':'Odoo','Type':'Business'}
def printDictionary(dictonary):
    for key in dictonary:
        print(key +"="+ str(dictonary[key]))
print(printDictionary(software))