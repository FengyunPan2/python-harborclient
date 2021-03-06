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


class RepTargetPost(object):
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
        'endpoint': 'str',
        'name': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'name': 'name',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, endpoint=None, name=None, username=None, password=None):
        """
        RepTargetPost - a model defined in Swagger
        """

        self._endpoint = None
        self._name = None
        self._username = None
        self._password = None

        if endpoint is not None:
          self.endpoint = endpoint
        if name is not None:
          self.name = name
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password

    @property
    def endpoint(self):
        """
        Gets the endpoint of this RepTargetPost.
        The target address URL string.

        :return: The endpoint of this RepTargetPost.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this RepTargetPost.
        The target address URL string.

        :param endpoint: The endpoint of this RepTargetPost.
        :type: str
        """

        self._endpoint = endpoint

    @property
    def name(self):
        """
        Gets the name of this RepTargetPost.
        The target name.

        :return: The name of this RepTargetPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RepTargetPost.
        The target name.

        :param name: The name of this RepTargetPost.
        :type: str
        """

        self._name = name

    @property
    def username(self):
        """
        Gets the username of this RepTargetPost.
        The target server username.

        :return: The username of this RepTargetPost.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this RepTargetPost.
        The target server username.

        :param username: The username of this RepTargetPost.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this RepTargetPost.
        The target server password.

        :return: The password of this RepTargetPost.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this RepTargetPost.
        The target server password.

        :param password: The password of this RepTargetPost.
        :type: str
        """

        self._password = password

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
        if not isinstance(other, RepTargetPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
