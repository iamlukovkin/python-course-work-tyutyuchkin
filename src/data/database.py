import json


json_path: str = "src/data/database.json"


def read_json() -> dict:
    result: dict = {}
    with open(json_path, 'r') as file:
        json_database = json.load(file)
    for key, value in json_database.items():
        result[int(key)] = value
    return result


def write_json() -> None:
    json_database = {str(key): value for key, value in database.items()}
    with open(json_path, 'w') as file:
        json.dump(json_database, file, ensure_ascii=False)


database: dict = read_json()
