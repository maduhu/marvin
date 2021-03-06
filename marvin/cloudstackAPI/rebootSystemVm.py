"""Reboots a system VM."""
from baseCmd import *
from baseResponse import *


class rebootSystemVmCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The ID of the system virtual machine"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class rebootSystemVmResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the system VM"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the number of active console sessions for the console proxy system vm"""
        self.activeviewersessions = None
        self.typeInfo['activeviewersessions'] = 'integer'
        """the date and time the system VM was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the first DNS for the system VM"""
        self.dns1 = None
        self.typeInfo['dns1'] = 'string'
        """the second DNS for the system VM"""
        self.dns2 = None
        self.typeInfo['dns2'] = 'string'
        """the gateway for the system VM"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the host ID for the system VM"""
        self.hostid = None
        self.typeInfo['hostid'] = 'string'
        """the hostname for the system VM"""
        self.hostname = None
        self.typeInfo['hostname'] = 'string'
        """the hypervisor on which the template runs"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """the job ID associated with the system VM. This is only displayed if the router listed is part of a currently running asynchronous job."""
        self.jobid = None
        self.typeInfo['jobid'] = 'string'
        """the job status associated with the system VM.  This is only displayed if the router listed is part of a currently running asynchronous job."""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = 'integer'
        """the link local IP address for the system vm"""
        self.linklocalip = None
        self.typeInfo['linklocalip'] = 'string'
        """the link local MAC address for the system vm"""
        self.linklocalmacaddress = None
        self.typeInfo['linklocalmacaddress'] = 'string'
        """the link local netmask for the system vm"""
        self.linklocalnetmask = None
        self.typeInfo['linklocalnetmask'] = 'string'
        """the name of the system VM"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the network domain for the system VM"""
        self.networkdomain = None
        self.typeInfo['networkdomain'] = 'string'
        """the Pod ID for the system VM"""
        self.podid = None
        self.typeInfo['podid'] = 'string'
        """the private IP address for the system VM"""
        self.privateip = None
        self.typeInfo['privateip'] = 'string'
        """the private MAC address for the system VM"""
        self.privatemacaddress = None
        self.typeInfo['privatemacaddress'] = 'string'
        """the private netmask for the system VM"""
        self.privatenetmask = None
        self.typeInfo['privatenetmask'] = 'string'
        """the public IP address for the system VM"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """the public MAC address for the system VM"""
        self.publicmacaddress = None
        self.typeInfo['publicmacaddress'] = 'string'
        """the public netmask for the system VM"""
        self.publicnetmask = None
        self.typeInfo['publicnetmask'] = 'string'
        """the state of the system VM"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the system VM type"""
        self.systemvmtype = None
        self.typeInfo['systemvmtype'] = 'string'
        """the template ID for the system VM"""
        self.templateid = None
        self.typeInfo['templateid'] = 'string'
        """the Zone ID for the system VM"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name for the system VM"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'

