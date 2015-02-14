from jenkins_master import JenkinsMaster
from elasticsearch_host import ElasticsearchHost

class DataSync(object):
    def __init__(self, master, eshost):
        self._master = master
        self._eshost = eshost
    
    def sync_data(self, job_name):
        print 'Processing %s into elasticsearch' % job_name
        build_ids = self._master.get_build_ids(job_name)
        for build_id in build_ids:
            print 'Processing %s #%s' % (job_name, build_id)
            data = self._master.get_build_data(job_name, build_id)
            self._eshost.inject_data(self._master.get_name(), job_name, data)
            
if __name__ == '__main__':
    master = JenkinsMaster('test-master', 'http://localhost:8080')
    eshost = ElasticsearchHost('localhost:9200')
    sync = DataSync(master, eshost)
    sync.sync_data('test-job-1')