"""Creates and automatically starts a virtual machine based on a service offering, disk offering, and template."""
from baseCmd import *
from baseResponse import *


class deployVirtualMachineCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the service offering for the virtual machine"""
        """Required"""
        self.serviceofferingid = None
        self.typeInfo['serviceofferingid'] = 'uuid'
        """the ID of the template for the virtual machine"""
        """Required"""
        self.templateid = None
        self.typeInfo['templateid'] = 'uuid'
        """availability zone for the virtual machine"""
        """Required"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        """an optional account for the virtual machine. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """comma separated list of affinity groups id that are going to be applied to the virtual machine. Mutually exclusive with affinitygroupnames parameter"""
        self.affinitygroupids = []
        self.typeInfo['affinitygroupids'] = 'list'
        """comma separated list of affinity groups names that are going to be applied to the virtual machine.Mutually exclusive with affinitygroupids parameter"""
        self.affinitygroupnames = []
        self.typeInfo['affinitygroupnames'] = 'list'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """Deployment planner to use for vm allocation. Available to ROOT admin only"""
        self.deploymentplanner = None
        self.typeInfo['deploymentplanner'] = 'string'
        """used to specify the custom parameters."""
        self.details = []
        self.typeInfo['details'] = 'map'
        """the ID of the disk offering for the virtual machine. If the template is of ISO format, the diskOfferingId is for the root disk volume. Otherwise this parameter is used to indicate the offering for the data disk volume. If the templateId parameter passed is from a Template object, the diskOfferingId refers to a DATA Disk Volume created. If the templateId parameter passed is from an ISO object, the diskOfferingId refers to a ROOT Disk Volume created."""
        self.diskofferingid = None
        self.typeInfo['diskofferingid'] = 'uuid'
        """an optional user generated name for the virtual machine"""
        self.displayname = None
        self.typeInfo['displayname'] = 'string'
        """an optional field, whether to the display the vm to the end user or not."""
        self.displayvm = None
        self.typeInfo['displayvm'] = 'boolean'
        """an optional domainId for the virtual machine. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """an optional group for the virtual machine"""
        self.group = None
        self.typeInfo['group'] = 'string'
        """destination Host ID to deploy the VM to - parameter available for root admin only"""
        self.hostid = None
        self.typeInfo['hostid'] = 'uuid'
        """the hypervisor on which to deploy the virtual machine. The parameter is required and respected only when hypervisor info is not set on the ISO/Template passed to the call"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """the ipv6 address for default vm's network"""
        self.ip6address = None
        self.typeInfo['ip6address'] = 'string'
        """the ip address for default vm's network"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """ip to network mapping. Can't be specified with networkIds parameter. Example: iptonetworklist[0].ip=10.10.10.11&iptonetworklist[0].ipv6=fc00:1234:5678::abcd&iptonetworklist[0].networkid=uuid - requests to use ip 10.10.10.11 in network id=uuid"""
        self.iptonetworklist = []
        self.typeInfo['iptonetworklist'] = 'map'
        """an optional keyboard device type for the virtual machine. valid value can be one of de,de-ch,es,fi,fr,fr-be,fr-ch,is,it,jp,nl-be,no,pt,uk,us"""
        self.keyboard = None
        self.typeInfo['keyboard'] = 'string'
        """name of the ssh key pair used to login to the virtual machine"""
        self.keypair = None
        self.typeInfo['keypair'] = 'string'
        """host name for the virtual machine"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """list of network ids used by virtual machine. Can't be specified with ipToNetworkList parameter"""
        self.networkids = []
        self.typeInfo['networkids'] = 'list'
        """Deploy vm for the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """Optional field to resize root disk on deploy. Value is in GB. Only applies to template-based deployments. Analogous to details[0].rootdisksize, which takes precedence over this parameter if both are provided"""
        self.rootdisksize = None
        self.typeInfo['rootdisksize'] = 'long'
        """comma separated list of security groups id that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupnames parameter"""
        self.securitygroupids = []
        self.typeInfo['securitygroupids'] = 'list'
        """comma separated list of security groups names that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support. Mutually exclusive with securitygroupids parameter"""
        self.securitygroupnames = []
        self.typeInfo['securitygroupnames'] = 'list'
        """the arbitrary size for the DATADISK volume. Mutually exclusive with diskOfferingId"""
        self.size = None
        self.typeInfo['size'] = 'long'
        """true if start vm after creating; defaulted to true if not specified"""
        self.startvm = None
        self.typeInfo['startvm'] = 'boolean'
        """an optional binary data that can be sent to the virtual machine upon a successful deployment. This binary data must be base64 encoded before adding it to the request. Using HTTP GET (via querystring), you can send up to 2KB of data after base64 encoding. Using HTTP POST(via POST body), you can send up to 32K of data after base64 encoding."""
        self.userdata = None
        self.typeInfo['userdata'] = 'string'
        self.required = ["serviceofferingid", "templateid", "zoneid", ]


class deployVirtualMachineResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the virtual machine"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the virtual machine"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the number of cpu this virtual machine is running with"""
        self.cpunumber = None
        self.typeInfo['cpunumber'] = 'integer'
        """the speed of each cpu"""
        self.cpuspeed = None
        self.typeInfo['cpuspeed'] = 'integer'
        """the amount of the vm's CPU currently used"""
        self.cpuused = None
        self.typeInfo['cpuused'] = 'string'
        """the date when this virtual machine was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """Vm details in key/value pairs."""
        self.details = None
        self.typeInfo['details'] = 'map'
        """the read (io) of disk on the vm"""
        self.diskioread = None
        self.typeInfo['diskioread'] = 'long'
        """the write (io) of disk on the vm"""
        self.diskiowrite = None
        self.typeInfo['diskiowrite'] = 'long'
        """the read (bytes) of disk on the vm"""
        self.diskkbsread = None
        self.typeInfo['diskkbsread'] = 'long'
        """the write (bytes) of disk on the vm"""
        self.diskkbswrite = None
        self.typeInfo['diskkbswrite'] = 'long'
        """the ID of the disk offering of the virtual machine"""
        self.diskofferingid = None
        self.typeInfo['diskofferingid'] = 'string'
        """the name of the disk offering of the virtual machine"""
        self.diskofferingname = None
        self.typeInfo['diskofferingname'] = 'string'
        """user generated name. The name of the virtual machine is returned if no displayname exists."""
        self.displayname = None
        self.typeInfo['displayname'] = 'string'
        """an optional field whether to the display the vm to the end user or not."""
        self.displayvm = None
        self.typeInfo['displayvm'] = 'boolean'
        """the name of the domain in which the virtual machine exists"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain in which the virtual machine exists"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the virtual network for the service offering"""
        self.forvirtualnetwork = None
        self.typeInfo['forvirtualnetwork'] = 'boolean'
        """the group name of the virtual machine"""
        self.group = None
        self.typeInfo['group'] = 'string'
        """the group ID of the virtual machine"""
        self.groupid = None
        self.typeInfo['groupid'] = 'string'
        """Os type ID of the virtual machine"""
        self.guestosid = None
        self.typeInfo['guestosid'] = 'string'
        """true if high-availability is enabled, false otherwise"""
        self.haenable = None
        self.typeInfo['haenable'] = 'boolean'
        """the ID of the host for the virtual machine"""
        self.hostid = None
        self.typeInfo['hostid'] = 'string'
        """the name of the host for the virtual machine"""
        self.hostname = None
        self.typeInfo['hostname'] = 'string'
        """the hypervisor on which the template runs"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """instance name of the user vm; this parameter is returned to the ROOT admin only"""
        self.instancename = None
        self.typeInfo['instancename'] = 'string'
        """true if vm contains XS tools inorder to support dynamic scaling of VM cpu/memory."""
        self.isdynamicallyscalable = None
        self.typeInfo['isdynamicallyscalable'] = 'boolean'
        """an alternate display text of the ISO attached to the virtual machine"""
        self.isodisplaytext = None
        self.typeInfo['isodisplaytext'] = 'string'
        """the ID of the ISO attached to the virtual machine"""
        self.isoid = None
        self.typeInfo['isoid'] = 'string'
        """the name of the ISO attached to the virtual machine"""
        self.isoname = None
        self.typeInfo['isoname'] = 'string'
        """ssh key-pair"""
        self.keypair = None
        self.typeInfo['keypair'] = 'string'
        """the memory allocated for the virtual machine"""
        self.memory = None
        self.typeInfo['memory'] = 'integer'
        """the name of the virtual machine"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the incoming network traffic on the vm"""
        self.networkkbsread = None
        self.typeInfo['networkkbsread'] = 'long'
        """the outgoing network traffic on the host"""
        self.networkkbswrite = None
        self.typeInfo['networkkbswrite'] = 'long'
        """OS type id of the vm"""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'long'
        """the password (if exists) of the virtual machine"""
        self.password = None
        self.typeInfo['password'] = 'string'
        """true if the password rest feature is enabled, false otherwise"""
        self.passwordenabled = None
        self.typeInfo['passwordenabled'] = 'boolean'
        """the project name of the vm"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the vm"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """public IP address id associated with vm via Static nat rule"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """public IP address id associated with vm via Static nat rule"""
        self.publicipid = None
        self.typeInfo['publicipid'] = 'string'
        """device ID of the root volume"""
        self.rootdeviceid = None
        self.typeInfo['rootdeviceid'] = 'long'
        """device type of the root volume"""
        self.rootdevicetype = None
        self.typeInfo['rootdevicetype'] = 'string'
        """the ID of the service offering of the virtual machine"""
        self.serviceofferingid = None
        self.typeInfo['serviceofferingid'] = 'string'
        """the name of the service offering of the virtual machine"""
        self.serviceofferingname = None
        self.typeInfo['serviceofferingname'] = 'string'
        """State of the Service from LB rule"""
        self.servicestate = None
        self.typeInfo['servicestate'] = 'string'
        """the state of the virtual machine"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """an alternate display text of the template for the virtual machine"""
        self.templatedisplaytext = None
        self.typeInfo['templatedisplaytext'] = 'string'
        """the ID of the template for the virtual machine. A -1 is returned if the virtual machine was created from an ISO file."""
        self.templateid = None
        self.typeInfo['templateid'] = 'string'
        """the name of the template for the virtual machine"""
        self.templatename = None
        self.typeInfo['templatename'] = 'string'
        """the user's ID who deployed the virtual machine"""
        self.userid = None
        self.typeInfo['userid'] = 'string'
        """the user's name who deployed the virtual machine"""
        self.username = None
        self.typeInfo['username'] = 'string'
        """the vgpu type used by the virtual machine"""
        self.vgpu = None
        self.typeInfo['vgpu'] = 'string'
        """the ID of the availablility zone for the virtual machine"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the name of the availability zone for the virtual machine"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """list of affinity groups associated with the virtual machine"""
        self.affinitygroup = []
        """the list of nics associated with vm"""
        self.nic = []
        """list of security groups associated with the virtual machine"""
        self.securitygroup = []
        """the list of resource tags associated with vm"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

class affinitygroup:
    def __init__(self):
        """"the ID of the affinity group"""
        self.id = None
        """"the account owning the affinity group"""
        self.account = None
        """"the description of the affinity group"""
        self.description = None
        """"the domain name of the affinity group"""
        self.domain = None
        """"the domain ID of the affinity group"""
        self.domainid = None
        """"the name of the affinity group"""
        self.name = None
        """"the project name of the affinity group"""
        self.project = None
        """"the project ID of the affinity group"""
        self.projectid = None
        """"the type of the affinity group"""
        self.type = None
        """"virtual machine IDs associated with this affinity group"""
        self.virtualmachineIds = None

class nic:
    def __init__(self):
        """"the ID of the nic"""
        self.id = None
        """"the broadcast uri of the nic"""
        self.broadcasturi = None
        """"device id for the network when plugged into the virtual machine"""
        self.deviceid = None
        """"the gateway of the nic"""
        self.gateway = None
        """"the IPv6 address of network"""
        self.ip6address = None
        """"the cidr of IPv6 network"""
        self.ip6cidr = None
        """"the gateway of IPv6 network"""
        self.ip6gateway = None
        """"the ip address of the nic"""
        self.ipaddress = None
        """"true if nic is default, false otherwise"""
        self.isdefault = None
        """"the isolation uri of the nic"""
        self.isolationuri = None
        """"true if nic is default, false otherwise"""
        self.macaddress = None
        """"the netmask of the nic"""
        self.netmask = None
        """"the ID of the corresponding network"""
        self.networkid = None
        """"the name of the corresponding network"""
        self.networkname = None
        """"the Secondary ipv4 addr of nic"""
        self.secondaryip = None
        """"the traffic type of the nic"""
        self.traffictype = None
        """"the type of the nic"""
        self.type = None
        """"Id of the vm to which the nic belongs"""
        self.virtualmachineid = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class egressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class ingressrule:
    def __init__(self):
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

class securitygroup:
    def __init__(self):
        """"the ID of the security group"""
        self.id = None
        """"the account owning the security group"""
        self.account = None
        """"the description of the security group"""
        self.description = None
        """"the domain name of the security group"""
        self.domain = None
        """"the domain ID of the security group"""
        self.domainid = None
        """"the name of the security group"""
        self.name = None
        """"the project name of the group"""
        self.project = None
        """"the project id of the group"""
        self.projectid = None
        """"the number of virtualmachines associated with this securitygroup"""
        self.virtualmachinecount = None
        """"the list of virtualmachine ids associated with this securitygroup"""
        self.virtualmachineids = None
        """"the list of egress rules associated with the security group"""
        self.egressrule = []
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None
        """"the list of ingress rules associated with the security group"""
        self.ingressrule = []
        """"account owning the security group rule"""
        self.account = None
        """"the CIDR notation for the base IP address of the security group rule"""
        self.cidr = None
        """"the ending IP of the security group rule"""
        self.endport = None
        """"the code for the ICMP message response"""
        self.icmpcode = None
        """"the type of the ICMP message response"""
        self.icmptype = None
        """"the protocol of the security group rule"""
        self.protocol = None
        """"the id of the security group rule"""
        self.ruleid = None
        """"security group name"""
        self.securitygroupname = None
        """"the starting IP of the security group rule"""
        self.startport = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None
        """"the list of resource tags associated with the rule"""
        self.tags = []
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None
        """"the ID of the latest async job acting on this object"""
        self.jobid = None
        """"the current status of the latest async job acting on this object"""
        self.jobstatus = None

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

