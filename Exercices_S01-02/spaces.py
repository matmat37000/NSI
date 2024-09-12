import requests  # le module requests permet de faire des requetes sur internet
import folium
from functools import lru_cache


@lru_cache(maxsize=None)
def get_API(url: str, API: str = "", *args) -> dict:
    """
    affiche le temps de la ville
    """
    # url = f'http://api.open-notify.org/astros.json'
    # proxy = {"http": "proxy:8080"}

    # cette fonction admet 2 arguments : url et [proxies]
    r = requests.get(url)
    return r.json()


def part1() -> None:

    @lru_cache(maxsize=None)
    def people_in_space() -> (list[str], int):
        results: dict = get_API("http://api.open-notify.org/astros.json")
        people: list[str] = []
        count: int = 0
        for result in results.get("people"):
            if result["craft"] == "ISS":
                people.append(result["name"])
                count += 1

        return people, count

    people = people_in_space()
    names = people[0]
    print(
        f"Il y a actuellement {people[1]} personne.s dans l'espace et l'ISS, ", end=""
    )
    for i in range(len(names)):
        print(names[i], end="")
        if i != len(names) - 1:
            print(", ", end="")
    print(".")


def part2():
    def position() -> (float, float):
        results: dict = get_API("http://api.open-notify.org/iss-now.json")
        latitude: float = results["iss_position"]["latitude"]
        longitude: float = results["iss_position"]["longitude"]

        return (latitude, longitude)

    m = folium.Map(location=position())

    folium.Marker(
        location=list(position()),
        tooltip="ISS",
        popup="ISS Location",
        icon=folium.Icon(icon="cloud"),
    ).add_to(m)
    m.save("index.html")


part2()
