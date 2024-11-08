import json

import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action= "store", default= "uat")

def update_env(config):
    with open("D:\\Source\\Python\\Automation\\Framework\\BackendFramework\\API_Framework\\config\\endpoints.json") as end_point:
        data = json.load(end_point)
        end_point.truncate(0)
        end_point.seek(0)
        data['environment']['env'] = config.getoption("--host").lower()
        json.dump(data, end_point, indent=4)
        end_point.close()

@pytest.hookimpl
def pytest_configure(config):
    update_env(config)




