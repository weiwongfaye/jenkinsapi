import os

class testConfig(object):
    def __init__(self, baseurl, username=None, password=None, proxyhost=None, proxyport=None, proxyuser=None, proxypass=None, formauth=False):
        self.baseurl=baseurl
        self.username=username
        self.password=password
        self.proxyhost=proxyhost
        self.proxyuser=proxyuser
        self.proxypass=proxypass
        self.formauth=formauth
        
baseurl = os.environ.get("JENKINS_URL", "http://localhost:8080")
        
defaultConfig=testConfig(baseurl)