import json
from multiprocessing import process
from pprint import pprint


def load_json(filename):
    with open(filename) as f:
        return json.load(f)


def process_skin_type(skin_type):
    smol_name_file = f"src/data/{skin_type}.json"
    big_name_file = f"src/data/{skin_type}_caps.json"

    smol_names = load_json(smol_name_file)
    big_names = load_json(big_name_file)

    all_urls = set([v for v in smol_names.values()])
    all_urls.update([v for v in big_names.values()])

    smol_vals = {v: k for k, v in smol_names.items()}
    big_vals = {v: k for k, v in big_names.items()}

    name_map = {smol_vals[url]: big_vals[url] for url in all_urls}

    return name_map


vandals = process_skin_type("vandal")
phantoms = process_skin_type("phantom")

all_skins = {**vandals, **phantoms}
all_skins = dict(sorted(all_skins.items()))
all_skins_json = json.dumps(all_skins, indent=4)
pprint(all_skins_json)
