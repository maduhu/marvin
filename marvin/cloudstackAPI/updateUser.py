"""Updates a user account"""
from baseCmd import *
from baseResponse import *


class updateUserCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """User uuid"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """email"""
        self.email = None
        self.typeInfo['email'] = 'string'
        """first name"""
        self.firstname = None
        self.typeInfo['firstname'] = 'string'
        """last name"""
        self.lastname = None
        self.typeInfo['lastname'] = 'string'
        """Clear text password (default hashed to SHA256SALT). If you wish to use any other hasing algorithm, you would need to write a custom authentication adapter"""
        self.password = None
        self.typeInfo['password'] = 'string'
        """Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format."""
        self.timezone = None
        self.typeInfo['timezone'] = 'string'
        """The API key for the user. Must be specified with userSecretKey"""
        self.userapikey = None
        self.typeInfo['userapikey'] = 'string'
        """Unique username"""
        self.username = None
        self.typeInfo['username'] = 'string'
        """The secret key for the user. Must be specified with userSecretKey"""
        self.usersecretkey = None
        self.typeInfo['usersecretkey'] = 'string'
        self.required = ["id", ]


class updateUserResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the user ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account name of the user"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the account ID of the user"""
        self.accountid = None
        self.typeInfo['accountid'] = 'string'
        """the account type of the user"""
        self.accounttype = None
        self.typeInfo['accounttype'] = 'short'
        """the api key of the user"""
        self.apikey = None
        self.typeInfo['apikey'] = 'string'
        """the date and time the user account was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the domain name of the user"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID of the user"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the user email address"""
        self.email = None
        self.typeInfo['email'] = 'string'
        """the user firstname"""
        self.firstname = None
        self.typeInfo['firstname'] = 'string'
        """the boolean value representing if the updating target is in caller's child domain"""
        self.iscallerchilddomain = None
        self.typeInfo['iscallerchilddomain'] = 'boolean'
        """true if user is default, false otherwise"""
        self.isdefault = None
        self.typeInfo['isdefault'] = 'boolean'
        """the user lastname"""
        self.lastname = None
        self.typeInfo['lastname'] = 'string'
        """the secret key of the user"""
        self.secretkey = None
        self.typeInfo['secretkey'] = 'string'
        """the user state"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the timezone user was created in"""
        self.timezone = None
        self.typeInfo['timezone'] = 'string'
        """the user name"""
        self.username = None
        self.typeInfo['username'] = 'string'

