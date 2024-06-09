import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(login, title, description, content, find_description):
    header = {"X-Auth-Token": login}
    res1 = requests.post(data["address2"], params={"title": title, "description": description, "content": content},
                         headers=header)
    res2 = requests.get(data["address2"], params={"description": find_description}, headers=header)
    assert res1 and res2, "test_2 failed"
