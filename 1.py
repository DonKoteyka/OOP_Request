import requests
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'
super_hero = ['Hulk', 'Captain America', 'Thanos']
def sh_intellegesce(url, super_hero):
    respond = requests.get(url).json()
    index_hero = [i for i in range(len(respond)) if respond[i].get('name') in super_hero]
    most_intellegence_hero = sorted([(respond[x].get('powerstats').get('intelligence'), respond[x].get('name')) for x in index_hero], key=lambda y: y[0], reverse=True)

    return most_intellegence_hero[0][1]
pprint(sh_intellegesce(url, super_hero))



