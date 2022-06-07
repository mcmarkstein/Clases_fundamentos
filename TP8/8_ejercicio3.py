'''
 Search cocktail by name
● Search by ingredient
● Lookup full cocktail details by id
Desarrollar un programa que nos permita consumir los diferentes servicios, buscando un
cocktail por nombre, o un cocktail por ingrediente. Será recomendable desarrollar un menú
para poder solicitar y ver los cocktails mas dinamicamente.
'''
import requests

url_cocktail_name = "www.thecocktaildb.com/api/json/v1/1/search.php"
url_cocktail_ingredient = "http://www.thecocktaildb.com/api/json/v1/1/search.php"
url_cocktail_id = "www.thecocktaildb.com/api/json/v1/1/lookup.php"

'''http_rsp = requests.get(url_cocktail_name, params= {'s': 'margarita'})

rsp_json = http_rsp.json())
print(type(rsp_json))
print(rsp_json['drinks'][0]['idDrink'])'''

class Drinks:
    def __init__(self, title,strAlcoholic, strInstructions):
        self.title = title
        self.strAlcoholic =strAlcoholic
        self.strInstructions = strInstructions

    def __str__(self):
        return f"El nombre {self.title}" \
                f"Es alcoholico: {self.strAlcoholic}" \
                f"Las intrucciones en ingles: {self.strInstructions}

print(Drink('T', 's', 's'))

drink_type = input('>> ')
req_params = {'s' : drink_type}
http_rsp = requests.get(url_cocktail_name, params= req_params)





