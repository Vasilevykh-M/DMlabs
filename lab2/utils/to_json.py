import json

def to_json(json_file):
    result = []
    for group in json_file:
            data = {
                "Название": group['name'],
                "Цена": float(group['price'].split(" ")[1][1:])
            }
            result.append(data)

    with open('result.json', 'w') as f:
        json.dump(result, f)
