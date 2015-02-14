from elasticsearch import Elasticsearch

class ElasticsearchHost(object):
    def __init__(self, elastic_host):
        self._elastichost = elastic_host
        self._elastic_client = Elasticsearch([self._elastichost])
        
    def inject_data(self, index, doc_type, data):
        '''
        index: master name
        type: job name
        data: build data
        '''
        self._elastic_client.index(index=index, doc_type=doc_type, id=data['number'], body=data)
        
