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


class DetailedTag(object):
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
        'digest': 'str',
        'name': 'str',
        'architecture': 'str',
        'os': 'str',
        'docker_version': 'str',
        'author': 'str',
        'created': 'str',
        'signature': 'object',
        'scan_overview': 'DetailedTagScanOverview'
    }

    attribute_map = {
        'digest': 'digest',
        'name': 'name',
        'architecture': 'architecture',
        'os': 'os',
        'docker_version': 'docker_version',
        'author': 'author',
        'created': 'created',
        'signature': 'signature',
        'scan_overview': 'scan_overview'
    }

    def __init__(self, digest=None, name=None, architecture=None, os=None, docker_version=None, author=None, created=None, signature=None, scan_overview=None):
        """
        DetailedTag - a model defined in Swagger
        """

        self._digest = None
        self._name = None
        self._architecture = None
        self._os = None
        self._docker_version = None
        self._author = None
        self._created = None
        self._signature = None
        self._scan_overview = None

        if digest is not None:
          self.digest = digest
        if name is not None:
          self.name = name
        if architecture is not None:
          self.architecture = architecture
        if os is not None:
          self.os = os
        if docker_version is not None:
          self.docker_version = docker_version
        if author is not None:
          self.author = author
        if created is not None:
          self.created = created
        if signature is not None:
          self.signature = signature
        if scan_overview is not None:
          self.scan_overview = scan_overview

    @property
    def digest(self):
        """
        Gets the digest of this DetailedTag.
        The digest of the tag.

        :return: The digest of this DetailedTag.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """
        Sets the digest of this DetailedTag.
        The digest of the tag.

        :param digest: The digest of this DetailedTag.
        :type: str
        """

        self._digest = digest

    @property
    def name(self):
        """
        Gets the name of this DetailedTag.
        The name of the tag.

        :return: The name of this DetailedTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DetailedTag.
        The name of the tag.

        :param name: The name of this DetailedTag.
        :type: str
        """

        self._name = name

    @property
    def architecture(self):
        """
        Gets the architecture of this DetailedTag.
        The architecture of the image.

        :return: The architecture of this DetailedTag.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this DetailedTag.
        The architecture of the image.

        :param architecture: The architecture of this DetailedTag.
        :type: str
        """

        self._architecture = architecture

    @property
    def os(self):
        """
        Gets the os of this DetailedTag.
        The os of the image.

        :return: The os of this DetailedTag.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this DetailedTag.
        The os of the image.

        :param os: The os of this DetailedTag.
        :type: str
        """

        self._os = os

    @property
    def docker_version(self):
        """
        Gets the docker_version of this DetailedTag.
        The version of docker which builds the image.

        :return: The docker_version of this DetailedTag.
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """
        Sets the docker_version of this DetailedTag.
        The version of docker which builds the image.

        :param docker_version: The docker_version of this DetailedTag.
        :type: str
        """

        self._docker_version = docker_version

    @property
    def author(self):
        """
        Gets the author of this DetailedTag.
        The author of the image.

        :return: The author of this DetailedTag.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this DetailedTag.
        The author of the image.

        :param author: The author of this DetailedTag.
        :type: str
        """

        self._author = author

    @property
    def created(self):
        """
        Gets the created of this DetailedTag.
        The build time of the image.

        :return: The created of this DetailedTag.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DetailedTag.
        The build time of the image.

        :param created: The created of this DetailedTag.
        :type: str
        """

        self._created = created

    @property
    def signature(self):
        """
        Gets the signature of this DetailedTag.
        The signature of image, defined by RepoSignature. If it is null, the image is unsigned.

        :return: The signature of this DetailedTag.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this DetailedTag.
        The signature of image, defined by RepoSignature. If it is null, the image is unsigned.

        :param signature: The signature of this DetailedTag.
        :type: object
        """

        self._signature = signature

    @property
    def scan_overview(self):
        """
        Gets the scan_overview of this DetailedTag.

        :return: The scan_overview of this DetailedTag.
        :rtype: DetailedTagScanOverview
        """
        return self._scan_overview

    @scan_overview.setter
    def scan_overview(self, scan_overview):
        """
        Sets the scan_overview of this DetailedTag.

        :param scan_overview: The scan_overview of this DetailedTag.
        :type: DetailedTagScanOverview
        """

        self._scan_overview = scan_overview

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
        if not isinstance(other, DetailedTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
