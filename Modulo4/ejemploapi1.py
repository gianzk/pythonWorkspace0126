import requests
url = "https://pokeapi.co/api/v2/pokemon"

response = requests.get(url)
print(response.status_code)
#formato api , json
data = response.json()

listaPokemons = data['results']
def getDataPokemon(url:str):
    dataP = requests.get(url)
    dataP = dataP.json()
    print(dataP)

for i in listaPokemons:
    if i['name']=='charizard':
        #getDataPokemon(i['url'])
        print(i['url'])

