from pathlib import Path
from pprint import pprint as print
import json
from latticejson.convert import latticejson_to_elegant, elegant_to_latticejson

base_dir = Path(__file__).resolve().parent / "data"
fodo_lte = (base_dir / "fodo.lte").read_text()
fodo_json = json.loads((base_dir / "fodo.json").read_text())


def test_latticejson_to_elegant():
    elegant = latticejson_to_elegant(fodo_json)
    print(elegant)


def test_elegant_to_latticejson():
    latticejson = elegant_to_latticejson(fodo_lte)
    print(latticejson)


## Uncomment to test for elegant examples
def test_all_elegant_examples():
    elegant_examples = Path.home() / "Git/elegant/examples"
    path_list = list(elegant_examples.rglob("*.lte"))
    for path in path_list:
        print(path)
        latticejson = elegant_to_latticejson(path.read_text())
        print(latticejson)
        input()
