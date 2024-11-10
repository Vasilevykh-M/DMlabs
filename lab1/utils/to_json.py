import json
def git_json_private(json_file):
    result = []
    for repo in json_file:
        if not repo["private"]:
            data = {
                "name": repo["name"],
                "owner": repo["owner"]["login"],
            }
            result.append(data)

    with open('result.json', 'w') as f:
        json.dump(result, f)

def vk_json_private(json_file):
    result = []
    for group in json_file:
            data = {
                "name": group['name'],
            }
            result.append(data)

    with open('result.json', 'w') as f:
        json.dump(result, f)
