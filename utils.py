import json


def load_candidates():
    with open("candidates.json") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["pk"]] = i
    return candidates




