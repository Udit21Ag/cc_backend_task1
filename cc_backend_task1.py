import sys
import requests

if len(sys.argv)!=2:
    print("Usage: python script.py <poke_name>")
    sys.exit(1)

poke_name=sys.argv[1]

def get_poke(poke_name):
    r=requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}")
    if r.status_code==200:
        return r.json()

def poke_abilities(poke_info):
    print("\nAbilities: ",end="")
    for i in poke_info["abilities"]:
        print(i["ability"]["name"].capitalize(),end=" ")

def poke_nn(poke_info):
    print(f"National Number: {poke_info["id"]}")

def poke_type(poke_info):
    print("Type: ",end="")
    for i in poke_info["types"]:
        print(i["type"]["name"].upper(),end=" ")

def poke_hnw(poke_info):
    print(f"\nHeight: {poke_info["height"]/10} m")
    print(f"Weight: {poke_info["weight"]/10} kg")

def poke_stat(poke_info):
    print("\nBase stats:")
    tot=0
    print(f"HP: {poke_info["stats"][0]["base_stat"]}")
    print(f"Attack: {poke_info["stats"][1]["base_stat"]}")
    print(f"Defense: {poke_info["stats"][2]["base_stat"]}")
    print(f"Special Attack: {poke_info["stats"][3]["base_stat"]}")
    print(f"Special Defense: {poke_info["stats"][4]["base_stat"]}")
    print(f"Speed: {poke_info["stats"][5]["base_stat"]}")
    for i in poke_info["stats"]:
        tot+=i["base_stat"]
    print(f"Total: {tot}")

def poke_img(poke_info):
    req=requests.get(poke_info["sprites"]["other"]["official-artwork"]["front_default"])
    with open("sprite.png", "wb") as f:
        f.write(req.content)

try:
    poke_abt=get_poke(poke_name)
    print(f"Name: {poke_abt["name"].capitalize()}")
    poke_nn(poke_abt)
    poke_type(poke_abt)
    poke_abilities(poke_abt)
    poke_hnw(poke_abt)
    poke_stat(poke_abt)
    print("Image downloaded")
    poke_img(poke_abt)


except Exception:
    print("Pokemon not found")