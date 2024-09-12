import requests  # le module requests permet de faire des requetes sur internet


def temps(clef, ville):
    """
    affiche le temps de la ville
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&units=metric&appid={clef}"
    proxy = {
        "http": "proxy:8080"
    }  # on ajoute une variable pour configurer le proxy du lycée
    r = requests.get(
        url, proxies=proxy
    )  # cette fonction admet 2 arguments : url et proxies (optionnel)
    return r.json()


temps_tours = temps("", "Tours")
print(temps_tours)


"""












print()
print(temps_tours["main"])
print()
print(temps_tours["main"]["temp"])


  """
