import json
from elasticsearch import Elasticsearch


es = Elasticsearch()

with open("dictionary_data.json", encoding='utf-8') as json_file:
    json_data = json.loads(json_file.read())

body = ""
for i in json_data:
    body = body + json.dumps({"index": {"_index": "dictionary", "_type": "dictionary_datas"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

es.bulk(body)