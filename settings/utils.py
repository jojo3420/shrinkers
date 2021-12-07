import json
from django.core.exceptions import ImproperlyConfigured


def read_json_env_file(path) -> dict:
    """ read json env file"""
    with open(path) as json_file:
        return json.load(json_file)


def get_env_val_by(dict_data: dict, key: str) -> str:
    if isinstance(dict_data, dict):
        try:
            return dict_data[key]
        except KeyError:
            raise ImproperlyConfigured(f'config key is not found => {key}')


if __name__ == '__main__':
    env_dict = read_json_env_file('env.json')
    print(get_env_val_by(env_dict, 'NAME1'))
