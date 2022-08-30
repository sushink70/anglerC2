import sys
import urllib.request
import netifaces 

def hostMachinePlatform():

    """Return the system platform of the host machine"""

    return sys.platform

def publicIP():

    """Return public IP address of the host machine"""

    ip = urllib.request.urlopen('https://api.ipify.org').read()
    ip = ip.decode('utf-8')
    return ip

def macAddress():

    """Return MAC Address of the host machine"""

    mac = netifaces.ifaddresses('eth0')
    mac = str(mac)
    return mac[16:33]

