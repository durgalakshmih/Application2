import platform
from datetime import date

def printtext():
#simple process to identify ID of the system, if --pid=host is added
#print("Hello World! I am running on", platform.node(), "and today is ", date.today())
##to identify host IP
  hostip= subprocess.run(ip route show | awk '/default/ {print $3}')
  print("Hello World! I am running on", $hostip, "and today is ", date.today())
