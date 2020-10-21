# search_app/setting_bulk.py


#import elasticsearch
from elasticsearch import Elasticsearch


es = Elasticsearch()


es.indices.create(
    index='dictionary',
    body={
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            }
        },
        "mappings": {
            "dictionary_datas": {
                "properties": {
                    "id": {
                        "type": "long"
                    },
                    "title": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    },
                    "content": {
                        "type": "text",
                        "analyzer": "my_analyzer"
                    }
                }
            }
        }
    }
)


