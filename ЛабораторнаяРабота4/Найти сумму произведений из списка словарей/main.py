
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, 'r') as input_f:
        json_data = json.load(input_f)
        return round(sum([elem["score"] * elem["weight"] for elem in json_data]), 3)



print(task())
