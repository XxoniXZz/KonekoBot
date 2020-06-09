import json
import logging


module_logger = logging.getLogger('koneko.json_storage_helper')


class JsonStorage:
    @staticmethod
    def write_json(data: any, filename='data.json',):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)


class PlayerStorage(JsonStorage):
    @staticmethod
    def save(user, p_race, p_class, p_name):
        with open('player.json', 'r') as f:
            data = json.load(f)

            obj = {
                user: {
                    'race': p_race,
                    'class': p_class,
                    'name': p_name
                }
            }

            data.update(obj)

            JsonStorage.write_json(data, 'player.json')

    @staticmethod
    def load(user):
        with open('player.json', 'r') as f:
            data = json.load(f)

            try:
                return data[str(user)]
            except KeyError:
                return False

    @staticmethod
    def delete(user):
        with open('player.json', 'r') as f:
            data = json.load(f)

            try:
                data.pop(str(user))
                JsonStorage.write_json(data, 'player.json')
                return True
            except KeyError:
                return False

