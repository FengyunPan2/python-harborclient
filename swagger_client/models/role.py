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


class Role(object):
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
        'role_id': 'int',
        'role_code': 'str',
        'role_name': 'str',
        'role_mask': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'role_code': 'role_code',
        'role_name': 'role_name',
        'role_mask': 'role_mask'
    }

    def __init__(self, role_id=None, role_code=None, role_name=None, role_mask=None):
        """
        Role - a model defined in Swagger
        """

        self._role_id = None
        self._role_code = None
        self._role_name = None
        self._role_mask = None

        if role_id is not None:
          self.role_id = role_id
        if role_code is not None:
          self.role_code = role_code
        if role_name is not None:
          self.role_name = role_name
        if role_mask is not None:
          self.role_mask = role_mask

    @property
    def role_id(self):
        """
        Gets the role_id of this Role.
        ID in table.

        :return: The role_id of this Role.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """
        Sets the role_id of this Role.
        ID in table.

        :param role_id: The role_id of this Role.
        :type: int
        """

        self._role_id = role_id

    @property
    def role_code(self):
        """
        Gets the role_code of this Role.
        Description of permissions for the role.

        :return: The role_code of this Role.
        :rtype: str
        """
        return self._role_code

    @role_code.setter
    def role_code(self, role_code):
        """
        Sets the role_code of this Role.
        Description of permissions for the role.

        :param role_code: The role_code of this Role.
        :type: str
        """

        self._role_code = role_code

    @property
    def role_name(self):
        """
        Gets the role_name of this Role.
        Name the the role.

        :return: The role_name of this Role.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """
        Sets the role_name of this Role.
        Name the the role.

        :param role_name: The role_name of this Role.
        :type: str
        """

        self._role_name = role_name

    @property
    def role_mask(self):
        """
        Gets the role_mask of this Role.

        :return: The role_mask of this Role.
        :rtype: str
        """
        return self._role_mask

    @role_mask.setter
    def role_mask(self, role_mask):
        """
        Sets the role_mask of this Role.

        :param role_mask: The role_mask of this Role.
        :type: str
        """

        self._role_mask = role_mask

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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
