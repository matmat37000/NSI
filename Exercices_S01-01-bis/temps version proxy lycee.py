import requests # le module requests permet de faire des requetes sur internet
import json
from datetime import datetime

def temps(API, *args):
    '''
    affiche le temps de la ville
    '''
    print(args)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={args[0]}&lon={args[1]}&appid={API}&units=metric'
    proxy = {"http":"proxy:8080"} # on ajoute une variable pour configurer le proxy du lycée
    r = requests.get(url) # cette fonction admet 2 arguments : url et proxies (optionnel)
    return r.json()
temps_tours=temps('',47.4371991,0.68595)
# print(temps_tours)
print(f"Vous êtes à {temps_tours["name"]}, il fait {temps_tours['main']['temp']}°c. Le soleil se couche à {datetime.fromtimestamp(temps_tours['sys']['sunset'])}")












"""



print()
print(temps_tours["main"])
print()
print(temps_tours["main"]["temp"])


  """    

