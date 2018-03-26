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


class AccessLog(object):
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
        'log_id': 'int',
        'username': 'str',
        'repo_name': 'str',
        'repo_tag': 'str',
        'operation': 'str',
        'op_time': 'str'
    }

    attribute_map = {
        'log_id': 'log_id',
        'username': 'username',
        'repo_name': 'repo_name',
        'repo_tag': 'repo_tag',
        'operation': 'operation',
        'op_time': 'op_time'
    }

    def __init__(self, log_id=None, username=None, repo_name=None, repo_tag=None, operation=None, op_time=None):
        """
        AccessLog - a model defined in Swagger
        """

        self._log_id = None
        self._username = None
        self._repo_name = None
        self._repo_tag = None
        self._operation = None
        self._op_time = None

        if log_id is not None:
          self.log_id = log_id
        if username is not None:
          self.username = username
        if repo_name is not None:
          self.repo_name = repo_name
        if repo_tag is not None:
          self.repo_tag = repo_tag
        if operation is not None:
          self.operation = operation
        if op_time is not None:
          self.op_time = op_time

    @property
    def log_id(self):
        """
        Gets the log_id of this AccessLog.
        The ID of the log entry.

        :return: The log_id of this AccessLog.
        :rtype: int
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """
        Sets the log_id of this AccessLog.
        The ID of the log entry.

        :param log_id: The log_id of this AccessLog.
        :type: int
        """

        self._log_id = log_id

    @property
    def username(self):
        """
        Gets the username of this AccessLog.
        Username of the user in this log entry.

        :return: The username of this AccessLog.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this AccessLog.
        Username of the user in this log entry.

        :param username: The username of this AccessLog.
        :type: str
        """

        self._username = username

    @property
    def repo_name(self):
        """
        Gets the repo_name of this AccessLog.
        Name of the repository in this log entry.

        :return: The repo_name of this AccessLog.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """
        Sets the repo_name of this AccessLog.
        Name of the repository in this log entry.

        :param repo_name: The repo_name of this AccessLog.
        :type: str
        """

        self._repo_name = repo_name

    @property
    def repo_tag(self):
        """
        Gets the repo_tag of this AccessLog.
        Tag of the repository in this log entry.

        :return: The repo_tag of this AccessLog.
        :rtype: str
        """
        return self._repo_tag

    @repo_tag.setter
    def repo_tag(self, repo_tag):
        """
        Sets the repo_tag of this AccessLog.
        Tag of the repository in this log entry.

        :param repo_tag: The repo_tag of this AccessLog.
        :type: str
        """

        self._repo_tag = repo_tag

    @property
    def operation(self):
        """
        Gets the operation of this AccessLog.
        The operation against the repository in this log entry.

        :return: The operation of this AccessLog.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this AccessLog.
        The operation against the repository in this log entry.

        :param operation: The operation of this AccessLog.
        :type: str
        """

        self._operation = operation

    @property
    def op_time(self):
        """
        Gets the op_time of this AccessLog.
        The time when this operation is triggered.

        :return: The op_time of this AccessLog.
        :rtype: str
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        """
        Sets the op_time of this AccessLog.
        The time when this operation is triggered.

        :param op_time: The op_time of this AccessLog.
        :type: str
        """

        self._op_time = op_time

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
        if not isinstance(other, AccessLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
