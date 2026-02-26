# how to connect to an API using python


import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
   url= f"{base_url}/pokeman/ {name}"
   response = requests.get(url)


   if response.status_code == 200:
     # pokeman_data = response.json()
      print("data retrieved !")
   else:
      print(f"failed to retrieve data {response.status_code}")


pokeman_name = "pikachu"
get_pokemon_info(pokeman_name)