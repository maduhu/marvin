"""Deletes an IP forwarding rule"""
from baseCmd import *
from baseResponse import *


class deleteIpForwardingRuleCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the forwarding rule"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteIpForwardingRuleResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

