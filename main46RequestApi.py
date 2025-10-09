# request pokemon API
# basically api nih data yang dh buat dekat pokemon so tarik jee takyah initiallize
import requests

base_url ="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    responce=requests.get(url)
    print(responce) # nih kalau responce 200 maksud dia okay website dia kalau 400 dia not found

    if responce.status_code == 200:
        pokemon_data=responce.json() # sbb ape guna json sbb senang boleh amik key value dia
        return pokemon_data
    else:
        print(f"Failed to retrive data {responce.status_code}")


pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")# yg nih kita amik key value name is pikachu lah tgk balik dictionary
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")