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


class UserProfile(object):
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
        'email': 'str',
        'realname': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'email': 'email',
        'realname': 'realname',
        'comment': 'comment'
    }

    def __init__(self, email=None, realname=None, comment=None):
        """
        UserProfile - a model defined in Swagger
        """

        self._email = None
        self._realname = None
        self._comment = None

        if email is not None:
          self.email = email
        if realname is not None:
          self.realname = realname
        if comment is not None:
          self.comment = comment

    @property
    def email(self):
        """
        Gets the email of this UserProfile.
        The new email.

        :return: The email of this UserProfile.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserProfile.
        The new email.

        :param email: The email of this UserProfile.
        :type: str
        """

        self._email = email

    @property
    def realname(self):
        """
        Gets the realname of this UserProfile.
        The new realname.

        :return: The realname of this UserProfile.
        :rtype: str
        """
        return self._realname

    @realname.setter
    def realname(self, realname):
        """
        Sets the realname of this UserProfile.
        The new realname.

        :param realname: The realname of this UserProfile.
        :type: str
        """

        self._realname = realname

    @property
    def comment(self):
        """
        Gets the comment of this UserProfile.
        The new comment.

        :return: The comment of this UserProfile.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this UserProfile.
        The new comment.

        :param comment: The comment of this UserProfile.
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
