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


class ComponentOverviewEntry(object):
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
        'severity': 'int',
        'count': 'int'
    }

    attribute_map = {
        'severity': 'severity',
        'count': 'count'
    }

    def __init__(self, severity=None, count=None):
        """
        ComponentOverviewEntry - a model defined in Swagger
        """

        self._severity = None
        self._count = None

        if severity is not None:
          self.severity = severity
        if count is not None:
          self.count = count

    @property
    def severity(self):
        """
        Gets the severity of this ComponentOverviewEntry.
        1-None/Negligible, 2-Unknown, 3-Low, 4-Medium, 5-High

        :return: The severity of this ComponentOverviewEntry.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this ComponentOverviewEntry.
        1-None/Negligible, 2-Unknown, 3-Low, 4-Medium, 5-High

        :param severity: The severity of this ComponentOverviewEntry.
        :type: int
        """

        self._severity = severity

    @property
    def count(self):
        """
        Gets the count of this ComponentOverviewEntry.
        number of the components with certain severity.

        :return: The count of this ComponentOverviewEntry.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this ComponentOverviewEntry.
        number of the components with certain severity.

        :param count: The count of this ComponentOverviewEntry.
        :type: int
        """

        self._count = count

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
        if not isinstance(other, ComponentOverviewEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
