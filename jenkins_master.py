import jenkinsapi
from data_injector import DataInjector

class JenkinsMaster(object):
    def __init__(self, name, url, user=None, password=None):
        self._name = name
        self._url = url
        self._user = user
        self._password = password
        self._api_client = jenkinsapi.jenkins.Jenkins(self._url, self._user, self._password)
        
    def get_name(self):
        return self._name
    
    def get_build_ids(self, job_name):
        if job_name not in self._api_client.keys():
            print 'Job %s does not exist.' % job_name
            return None
        else:
            return self._api_client[job_name].get_build_ids()
        
    def get_build_data(self, job_name, buid_number):
        # return None if job_name invalid
        if job_name not in self._api_client.keys():
            print 'Job %s does not exist.' % job_name
            return None
        else:
            job = self._api_client[job_name]
            
        if buid_number not in job.get_build_ids():
            print '%s #%s does not exist.' % (job_name, buid_number)
            return None
        else:
            build = job.get_build(buid_number)
            
        build._data['consoleLog'] = build.get_console()
        return build._data
