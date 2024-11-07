import json


class FunctionalParam:

    @staticmethod
    def get_base_end_point():
        with open("D:\\Source\\Python\\Automation\\Framework\\BackendFramework\\API_Framework\\config\\endpoints.json") as json_file:
            properties = json.load(json_file)
            env = properties["environment"]["env"]
            return properties[env]["base_url"]
