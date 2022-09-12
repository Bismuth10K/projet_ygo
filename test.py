from json_extractor import extract_values
from db_manager import *
import requests
import json
import sqlite3

response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Magicien sombre&language=fr").json()
# print(json.dumps(response, sort_keys=True, indent=4))
print(extract_values(response, 'name'))
# print(json.dumps(extract_values(response, 'card_sets'), sort_keys=True, indent=4))
# print(json.dumps(extract_values(response, 'card_sets')[0], sort_keys=True, indent=4))

add_card(response)

# response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?id=15862758&language=fr").json()
# print(json.dumps(response, sort_keys=True, indent=4))
# print(extract_values(response, 'name'))

get_posts()
