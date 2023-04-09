import requests
from pprint import pprint
url = 'https://akabab.github.io/superhero-api/api/all.json'
super_hero = ['Hulk', 'Captain America', 'Thanos']
def sh_intellegesce(url, super_hero):
    respond = requests.get(url).json()
    index_hero = [i for i in range(len(respond)) if respond[i].get('name') in super_hero]
    top_list = dict()
    for x in index_hero:
        if
        top_list.setdefault((respond[x].get('powerstats').get('intelligence')), [respond[x].get('name')])
        top_list[respond[x].get('powerstats').get('intelligence')].append(respond[x].get('name'))


    return top_list
pprint(sh_intellegesce(url, super_hero))



