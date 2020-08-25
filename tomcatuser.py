import subprocess
from checks import AgentCheck

__version__ = "0.0.2"

class CheckUser(AgentCheck):
    def check(self, instance):
        try:
            count = subprocess.check_output('netstat -na | find "TETETTE" | find /c /v ""', shell=True)
        except subprocess.CalledProcessError:
            count = 0
            self.gauge('Tomcat.User', count)
        else:
            self.gauge('Tomcat.User', count)

