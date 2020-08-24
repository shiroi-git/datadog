import subprocess
from checks import AgentCheck

__version__ = "0.0.2"

class CheckUser(AgentCheck):
    def check(self, instance):
        count = subprocess.check_output('netstat -na | find /c /v ""', shell=True)  
        self.gauge('Tomcat.User', count)

