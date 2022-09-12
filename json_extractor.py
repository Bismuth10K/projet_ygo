# Pour la bdd
import sqlite3
# Pour les requêtes web
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
# Pour adapter les résultats comme on le souhaite
import json


con = sqlite3.connect('ygo_db.sqlite')
cur = con.cursor()

response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?fname=ic1000&language=fr").json()
text = json.dumps(response, sort_keys=True, indent=4)

def extract_values(obj, key):
    # Extract nested values from a JSON tree.
    # Source https://hackersandslackers.com/extract-data-from-complex-json-python/
    # with modification from fjurg in github gist
    """Recursively fetch values from nested JSON."""
    arr = []
    def extractor(obj, arr, key):
        """Return all matching values in an object."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    if k == key:
                        arr.append(v)
                    extractor(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extractor(item, arr, key)
        return arr

    results = extractor(obj, arr, key)
    to_return = []
    for result in results:
        if type(result) == list:
            for item in result:
                to_return.append(item)
        else:
            to_return.append(result)
    return to_return
