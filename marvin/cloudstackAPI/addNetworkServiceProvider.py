"""Adds a network serviceProvider to a physical network"""
from baseCmd import *
from baseResponse import *


class addNetworkServiceProviderCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the name for the physical network service provider"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the Physical Network ID to add the provider to"""
        """Required"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        """the destination Physical Network ID to bridge to"""
        self.destinationphysicalnetworkid = None
        self.typeInfo['destinationphysicalnetworkid'] = 'uuid'
        """the list of services to be enabled for this physical network service provider"""
        self.servicelist = []
        self.typeInfo['servicelist'] = 'list'
        self.required = ["name", "physicalnetworkid", ]


class addNetworkServiceProviderResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """uuid of the network provider"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        self.typeInfo['canenableindividualservice'] = 'boolean'
        """the destination physical network"""
        self.destinationphysicalnetworkid = None
        self.typeInfo['destinationphysicalnetworkid'] = 'string'
        """the provider name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """services for this provider"""
        self.servicelist = None
        self.typeInfo['servicelist'] = 'list'
        """state of the network provider"""
        self.state = None
        self.typeInfo['state'] = 'string'

