# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Configurations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auth_mode': 'str',
        'email_from': 'str',
        'email_host': 'str',
        'email_port': 'int',
        'email_identity': 'str',
        'email_username': 'str',
        'email_ssl': 'bool',
        'ldap_url': 'str',
        'ldap_base_dn': 'str',
        'ldap_filter': 'str',
        'ldap_scope': 'int',
        'ldap_uid': 'str',
        'ldap_search_dn': 'str',
        'ldap_timeout': 'int',
        'project_creation_restriction': 'str',
        'self_registration': 'bool',
        'token_expiration': 'int',
        'verify_remote_cert': 'bool',
        'scan_all_policy': 'ConfigurationsScanAllPolicy'
    }

    attribute_map = {
        'auth_mode': 'auth_mode',
        'email_from': 'email_from',
        'email_host': 'email_host',
        'email_port': 'email_port',
        'email_identity': 'email_identity',
        'email_username': 'email_username',
        'email_ssl': 'email_ssl',
        'ldap_url': 'ldap_url',
        'ldap_base_dn': 'ldap_base_dn',
        'ldap_filter': 'ldap_filter',
        'ldap_scope': 'ldap_scope',
        'ldap_uid': 'ldap_uid',
        'ldap_search_dn': 'ldap_search_dn',
        'ldap_timeout': 'ldap_timeout',
        'project_creation_restriction': 'project_creation_restriction',
        'self_registration': 'self_registration',
        'token_expiration': 'token_expiration',
        'verify_remote_cert': 'verify_remote_cert',
        'scan_all_policy': 'scan_all_policy'
    }

    def __init__(self, auth_mode=None, email_from=None, email_host=None, email_port=None, email_identity=None, email_username=None, email_ssl=None, ldap_url=None, ldap_base_dn=None, ldap_filter=None, ldap_scope=None, ldap_uid=None, ldap_search_dn=None, ldap_timeout=None, project_creation_restriction=None, self_registration=None, token_expiration=None, verify_remote_cert=None, scan_all_policy=None):
        """
        Configurations - a model defined in Swagger
        """

        self._auth_mode = None
        self._email_from = None
        self._email_host = None
        self._email_port = None
        self._email_identity = None
        self._email_username = None
        self._email_ssl = None
        self._ldap_url = None
        self._ldap_base_dn = None
        self._ldap_filter = None
        self._ldap_scope = None
        self._ldap_uid = None
        self._ldap_search_dn = None
        self._ldap_timeout = None
        self._project_creation_restriction = None
        self._self_registration = None
        self._token_expiration = None
        self._verify_remote_cert = None
        self._scan_all_policy = None

        if auth_mode is not None:
          self.auth_mode = auth_mode
        if email_from is not None:
          self.email_from = email_from
        if email_host is not None:
          self.email_host = email_host
        if email_port is not None:
          self.email_port = email_port
        if email_identity is not None:
          self.email_identity = email_identity
        if email_username is not None:
          self.email_username = email_username
        if email_ssl is not None:
          self.email_ssl = email_ssl
        if ldap_url is not None:
          self.ldap_url = ldap_url
        if ldap_base_dn is not None:
          self.ldap_base_dn = ldap_base_dn
        if ldap_filter is not None:
          self.ldap_filter = ldap_filter
        if ldap_scope is not None:
          self.ldap_scope = ldap_scope
        if ldap_uid is not None:
          self.ldap_uid = ldap_uid
        if ldap_search_dn is not None:
          self.ldap_search_dn = ldap_search_dn
        if ldap_timeout is not None:
          self.ldap_timeout = ldap_timeout
        if project_creation_restriction is not None:
          self.project_creation_restriction = project_creation_restriction
        if self_registration is not None:
          self.self_registration = self_registration
        if token_expiration is not None:
          self.token_expiration = token_expiration
        if verify_remote_cert is not None:
          self.verify_remote_cert = verify_remote_cert
        if scan_all_policy is not None:
          self.scan_all_policy = scan_all_policy

    @property
    def auth_mode(self):
        """
        Gets the auth_mode of this Configurations.
        The auth mode of current system, such as \"db_auth\", \"ldap_auth\"

        :return: The auth_mode of this Configurations.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """
        Sets the auth_mode of this Configurations.
        The auth mode of current system, such as \"db_auth\", \"ldap_auth\"

        :param auth_mode: The auth_mode of this Configurations.
        :type: str
        """

        self._auth_mode = auth_mode

    @property
    def email_from(self):
        """
        Gets the email_from of this Configurations.
        The sender name for Email notification.

        :return: The email_from of this Configurations.
        :rtype: str
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """
        Sets the email_from of this Configurations.
        The sender name for Email notification.

        :param email_from: The email_from of this Configurations.
        :type: str
        """

        self._email_from = email_from

    @property
    def email_host(self):
        """
        Gets the email_host of this Configurations.
        The hostname of SMTP server that sends Email notification.

        :return: The email_host of this Configurations.
        :rtype: str
        """
        return self._email_host

    @email_host.setter
    def email_host(self, email_host):
        """
        Sets the email_host of this Configurations.
        The hostname of SMTP server that sends Email notification.

        :param email_host: The email_host of this Configurations.
        :type: str
        """

        self._email_host = email_host

    @property
    def email_port(self):
        """
        Gets the email_port of this Configurations.
        The port of SMTP server.

        :return: The email_port of this Configurations.
        :rtype: int
        """
        return self._email_port

    @email_port.setter
    def email_port(self, email_port):
        """
        Sets the email_port of this Configurations.
        The port of SMTP server.

        :param email_port: The email_port of this Configurations.
        :type: int
        """

        self._email_port = email_port

    @property
    def email_identity(self):
        """
        Gets the email_identity of this Configurations.
        By default it's empty so the email_username is picked.

        :return: The email_identity of this Configurations.
        :rtype: str
        """
        return self._email_identity

    @email_identity.setter
    def email_identity(self, email_identity):
        """
        Sets the email_identity of this Configurations.
        By default it's empty so the email_username is picked.

        :param email_identity: The email_identity of this Configurations.
        :type: str
        """

        self._email_identity = email_identity

    @property
    def email_username(self):
        """
        Gets the email_username of this Configurations.
        The username for authenticate against SMTP server.

        :return: The email_username of this Configurations.
        :rtype: str
        """
        return self._email_username

    @email_username.setter
    def email_username(self, email_username):
        """
        Sets the email_username of this Configurations.
        The username for authenticate against SMTP server.

        :param email_username: The email_username of this Configurations.
        :type: str
        """

        self._email_username = email_username

    @property
    def email_ssl(self):
        """
        Gets the email_ssl of this Configurations.
        When it's set to true the system will access Email server via TLS by default.  If it's set to false, it still will handle \"STARTTLS\" from server side.

        :return: The email_ssl of this Configurations.
        :rtype: bool
        """
        return self._email_ssl

    @email_ssl.setter
    def email_ssl(self, email_ssl):
        """
        Sets the email_ssl of this Configurations.
        When it's set to true the system will access Email server via TLS by default.  If it's set to false, it still will handle \"STARTTLS\" from server side.

        :param email_ssl: The email_ssl of this Configurations.
        :type: bool
        """

        self._email_ssl = email_ssl

    @property
    def ldap_url(self):
        """
        Gets the ldap_url of this Configurations.
        The URL of LDAP server.

        :return: The ldap_url of this Configurations.
        :rtype: str
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """
        Sets the ldap_url of this Configurations.
        The URL of LDAP server.

        :param ldap_url: The ldap_url of this Configurations.
        :type: str
        """

        self._ldap_url = ldap_url

    @property
    def ldap_base_dn(self):
        """
        Gets the ldap_base_dn of this Configurations.
        The Base DN for LDAP binding.

        :return: The ldap_base_dn of this Configurations.
        :rtype: str
        """
        return self._ldap_base_dn

    @ldap_base_dn.setter
    def ldap_base_dn(self, ldap_base_dn):
        """
        Sets the ldap_base_dn of this Configurations.
        The Base DN for LDAP binding.

        :param ldap_base_dn: The ldap_base_dn of this Configurations.
        :type: str
        """

        self._ldap_base_dn = ldap_base_dn

    @property
    def ldap_filter(self):
        """
        Gets the ldap_filter of this Configurations.
        The filter for LDAP binding.

        :return: The ldap_filter of this Configurations.
        :rtype: str
        """
        return self._ldap_filter

    @ldap_filter.setter
    def ldap_filter(self, ldap_filter):
        """
        Sets the ldap_filter of this Configurations.
        The filter for LDAP binding.

        :param ldap_filter: The ldap_filter of this Configurations.
        :type: str
        """

        self._ldap_filter = ldap_filter

    @property
    def ldap_scope(self):
        """
        Gets the ldap_scope of this Configurations.
        1-LDAP_SCOPE_BASE, 2-LDAP_SCOPE_ONELEVEL, 3-LDAP_SCOPE_SUBTREE

        :return: The ldap_scope of this Configurations.
        :rtype: int
        """
        return self._ldap_scope

    @ldap_scope.setter
    def ldap_scope(self, ldap_scope):
        """
        Sets the ldap_scope of this Configurations.
        1-LDAP_SCOPE_BASE, 2-LDAP_SCOPE_ONELEVEL, 3-LDAP_SCOPE_SUBTREE

        :param ldap_scope: The ldap_scope of this Configurations.
        :type: int
        """

        self._ldap_scope = ldap_scope

    @property
    def ldap_uid(self):
        """
        Gets the ldap_uid of this Configurations.
        The attribute which is used as identity for the LDAP binding, such as \"CN\" or \"SAMAccountname\"

        :return: The ldap_uid of this Configurations.
        :rtype: str
        """
        return self._ldap_uid

    @ldap_uid.setter
    def ldap_uid(self, ldap_uid):
        """
        Sets the ldap_uid of this Configurations.
        The attribute which is used as identity for the LDAP binding, such as \"CN\" or \"SAMAccountname\"

        :param ldap_uid: The ldap_uid of this Configurations.
        :type: str
        """

        self._ldap_uid = ldap_uid

    @property
    def ldap_search_dn(self):
        """
        Gets the ldap_search_dn of this Configurations.
        The DN of the user to do the search.

        :return: The ldap_search_dn of this Configurations.
        :rtype: str
        """
        return self._ldap_search_dn

    @ldap_search_dn.setter
    def ldap_search_dn(self, ldap_search_dn):
        """
        Sets the ldap_search_dn of this Configurations.
        The DN of the user to do the search.

        :param ldap_search_dn: The ldap_search_dn of this Configurations.
        :type: str
        """

        self._ldap_search_dn = ldap_search_dn

    @property
    def ldap_timeout(self):
        """
        Gets the ldap_timeout of this Configurations.
        timeout in seconds for connection to LDAP server.

        :return: The ldap_timeout of this Configurations.
        :rtype: int
        """
        return self._ldap_timeout

    @ldap_timeout.setter
    def ldap_timeout(self, ldap_timeout):
        """
        Sets the ldap_timeout of this Configurations.
        timeout in seconds for connection to LDAP server.

        :param ldap_timeout: The ldap_timeout of this Configurations.
        :type: int
        """

        self._ldap_timeout = ldap_timeout

    @property
    def project_creation_restriction(self):
        """
        Gets the project_creation_restriction of this Configurations.
        This attribute restricts what users have the permission to create project.  It can be \"everyone\" or \"adminonly\".

        :return: The project_creation_restriction of this Configurations.
        :rtype: str
        """
        return self._project_creation_restriction

    @project_creation_restriction.setter
    def project_creation_restriction(self, project_creation_restriction):
        """
        Sets the project_creation_restriction of this Configurations.
        This attribute restricts what users have the permission to create project.  It can be \"everyone\" or \"adminonly\".

        :param project_creation_restriction: The project_creation_restriction of this Configurations.
        :type: str
        """

        self._project_creation_restriction = project_creation_restriction

    @property
    def self_registration(self):
        """
        Gets the self_registration of this Configurations.
        Whether the Harbor instance supports self-registration.  If it's set to false, admin need to add user to the instance.

        :return: The self_registration of this Configurations.
        :rtype: bool
        """
        return self._self_registration

    @self_registration.setter
    def self_registration(self, self_registration):
        """
        Sets the self_registration of this Configurations.
        Whether the Harbor instance supports self-registration.  If it's set to false, admin need to add user to the instance.

        :param self_registration: The self_registration of this Configurations.
        :type: bool
        """

        self._self_registration = self_registration

    @property
    def token_expiration(self):
        """
        Gets the token_expiration of this Configurations.
        The expiration time of the token for internal Registry, in minutes.

        :return: The token_expiration of this Configurations.
        :rtype: int
        """
        return self._token_expiration

    @token_expiration.setter
    def token_expiration(self, token_expiration):
        """
        Sets the token_expiration of this Configurations.
        The expiration time of the token for internal Registry, in minutes.

        :param token_expiration: The token_expiration of this Configurations.
        :type: int
        """

        self._token_expiration = token_expiration

    @property
    def verify_remote_cert(self):
        """
        Gets the verify_remote_cert of this Configurations.
        Whether or not the certificate will be verified when Harbor tries to access a remote Harbor instance for replication.

        :return: The verify_remote_cert of this Configurations.
        :rtype: bool
        """
        return self._verify_remote_cert

    @verify_remote_cert.setter
    def verify_remote_cert(self, verify_remote_cert):
        """
        Sets the verify_remote_cert of this Configurations.
        Whether or not the certificate will be verified when Harbor tries to access a remote Harbor instance for replication.

        :param verify_remote_cert: The verify_remote_cert of this Configurations.
        :type: bool
        """

        self._verify_remote_cert = verify_remote_cert

    @property
    def scan_all_policy(self):
        """
        Gets the scan_all_policy of this Configurations.

        :return: The scan_all_policy of this Configurations.
        :rtype: ConfigurationsScanAllPolicy
        """
        return self._scan_all_policy

    @scan_all_policy.setter
    def scan_all_policy(self, scan_all_policy):
        """
        Sets the scan_all_policy of this Configurations.

        :param scan_all_policy: The scan_all_policy of this Configurations.
        :type: ConfigurationsScanAllPolicy
        """

        self._scan_all_policy = scan_all_policy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Configurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
