import requests
import json

DATAVERSE_ENDPOINT = "https://dataverse.harvard.edu/api/datasets/export"


def metadata(doi):
    rr = requests.get(DATAVERSE_ENDPOINT,
                      params={"exporter": "dataverse_json",
                              "persistentId": "doi:%s" % doi})
    meta = json.loads(rr.content.decode())
    return meta
