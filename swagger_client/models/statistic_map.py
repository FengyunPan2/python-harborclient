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


class StatisticMap(object):
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
        'private_project_count': 'int',
        'private_repo_count': 'int',
        'public_project_count': 'int',
        'public_repo_count': 'int',
        'total_project_count': 'int',
        'total_repo_count': 'int'
    }

    attribute_map = {
        'private_project_count': 'private_project_count',
        'private_repo_count': 'private_repo_count',
        'public_project_count': 'public_project_count',
        'public_repo_count': 'public_repo_count',
        'total_project_count': 'total_project_count',
        'total_repo_count': 'total_repo_count'
    }

    def __init__(self, private_project_count=None, private_repo_count=None, public_project_count=None, public_repo_count=None, total_project_count=None, total_repo_count=None):
        """
        StatisticMap - a model defined in Swagger
        """

        self._private_project_count = None
        self._private_repo_count = None
        self._public_project_count = None
        self._public_repo_count = None
        self._total_project_count = None
        self._total_repo_count = None

        if private_project_count is not None:
          self.private_project_count = private_project_count
        if private_repo_count is not None:
          self.private_repo_count = private_repo_count
        if public_project_count is not None:
          self.public_project_count = public_project_count
        if public_repo_count is not None:
          self.public_repo_count = public_repo_count
        if total_project_count is not None:
          self.total_project_count = total_project_count
        if total_repo_count is not None:
          self.total_repo_count = total_repo_count

    @property
    def private_project_count(self):
        """
        Gets the private_project_count of this StatisticMap.
        The count of the private projects which the user is a member of.

        :return: The private_project_count of this StatisticMap.
        :rtype: int
        """
        return self._private_project_count

    @private_project_count.setter
    def private_project_count(self, private_project_count):
        """
        Sets the private_project_count of this StatisticMap.
        The count of the private projects which the user is a member of.

        :param private_project_count: The private_project_count of this StatisticMap.
        :type: int
        """

        self._private_project_count = private_project_count

    @property
    def private_repo_count(self):
        """
        Gets the private_repo_count of this StatisticMap.
        The count of the private repositories belonging to the projects which the user is a member of.

        :return: The private_repo_count of this StatisticMap.
        :rtype: int
        """
        return self._private_repo_count

    @private_repo_count.setter
    def private_repo_count(self, private_repo_count):
        """
        Sets the private_repo_count of this StatisticMap.
        The count of the private repositories belonging to the projects which the user is a member of.

        :param private_repo_count: The private_repo_count of this StatisticMap.
        :type: int
        """

        self._private_repo_count = private_repo_count

    @property
    def public_project_count(self):
        """
        Gets the public_project_count of this StatisticMap.
        The count of the public projects.

        :return: The public_project_count of this StatisticMap.
        :rtype: int
        """
        return self._public_project_count

    @public_project_count.setter
    def public_project_count(self, public_project_count):
        """
        Sets the public_project_count of this StatisticMap.
        The count of the public projects.

        :param public_project_count: The public_project_count of this StatisticMap.
        :type: int
        """

        self._public_project_count = public_project_count

    @property
    def public_repo_count(self):
        """
        Gets the public_repo_count of this StatisticMap.
        The count of the public repositories belonging to the public projects which the user is a member of.

        :return: The public_repo_count of this StatisticMap.
        :rtype: int
        """
        return self._public_repo_count

    @public_repo_count.setter
    def public_repo_count(self, public_repo_count):
        """
        Sets the public_repo_count of this StatisticMap.
        The count of the public repositories belonging to the public projects which the user is a member of.

        :param public_repo_count: The public_repo_count of this StatisticMap.
        :type: int
        """

        self._public_repo_count = public_repo_count

    @property
    def total_project_count(self):
        """
        Gets the total_project_count of this StatisticMap.
        The count of the total projects, only be seen when the is admin.

        :return: The total_project_count of this StatisticMap.
        :rtype: int
        """
        return self._total_project_count

    @total_project_count.setter
    def total_project_count(self, total_project_count):
        """
        Sets the total_project_count of this StatisticMap.
        The count of the total projects, only be seen when the is admin.

        :param total_project_count: The total_project_count of this StatisticMap.
        :type: int
        """

        self._total_project_count = total_project_count

    @property
    def total_repo_count(self):
        """
        Gets the total_repo_count of this StatisticMap.
        The count of the total repositories, only be seen when the user is admin.

        :return: The total_repo_count of this StatisticMap.
        :rtype: int
        """
        return self._total_repo_count

    @total_repo_count.setter
    def total_repo_count(self, total_repo_count):
        """
        Sets the total_repo_count of this StatisticMap.
        The count of the total repositories, only be seen when the user is admin.

        :param total_repo_count: The total_repo_count of this StatisticMap.
        :type: int
        """

        self._total_repo_count = total_repo_count

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
        if not isinstance(other, StatisticMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
