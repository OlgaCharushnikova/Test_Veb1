import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def title():
    return "Title"

@pytest.fixture()
def description():
    return "Description"

@pytest.fixture()
def content():
    return "Content"

@pytest.fixture()
def find_description():
    return "Content"

