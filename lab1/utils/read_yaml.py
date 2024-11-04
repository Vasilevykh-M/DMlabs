import yaml

def read_yaml(file_name):
    with open(file_name) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)