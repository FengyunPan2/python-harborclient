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


class Project(object):
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
        'project_id': 'int',
        'owner_id': 'int',
        'name': 'str',
        'creation_time': 'str',
        'update_time': 'str',
        'deleted': 'int',
        'owner_name': 'str',
        'public': 'int',
        'togglable': 'bool',
        'current_user_role_id': 'int',
        'repo_count': 'int',
        'enable_content_trust': 'bool',
        'prevent_vulnerable_images_from_running': 'bool',
        'prevent_vulnerable_images_from_running_severity': 'str',
        'automatically_scan_images_on_push': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'owner_id': 'owner_id',
        'name': 'name',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'deleted': 'deleted',
        'owner_name': 'owner_name',
        'public': 'public',
        'togglable': 'Togglable',
        'current_user_role_id': 'current_user_role_id',
        'repo_count': 'repo_count',
        'enable_content_trust': 'enable_content_trust',
        'prevent_vulnerable_images_from_running': 'prevent_vulnerable_images_from_running',
        'prevent_vulnerable_images_from_running_severity': 'prevent_vulnerable_images_from_running_severity',
        'automatically_scan_images_on_push': 'automatically_scan_images_on_push'
    }

    def __init__(self, project_id=None, owner_id=None, name=None, creation_time=None, update_time=None, deleted=None, owner_name=None, public=None, togglable=None, current_user_role_id=None, repo_count=None, enable_content_trust=None, prevent_vulnerable_images_from_running=None, prevent_vulnerable_images_from_running_severity=None, automatically_scan_images_on_push=None):
        """
        Project - a model defined in Swagger
        """

        self._project_id = None
        self._owner_id = None
        self._name = None
        self._creation_time = None
        self._update_time = None
        self._deleted = None
        self._owner_name = None
        self._public = None
        self._togglable = None
        self._current_user_role_id = None
        self._repo_count = None
        self._enable_content_trust = None
        self._prevent_vulnerable_images_from_running = None
        self._prevent_vulnerable_images_from_running_severity = None
        self._automatically_scan_images_on_push = None

        if project_id is not None:
          self.project_id = project_id
        if owner_id is not None:
          self.owner_id = owner_id
        if name is not None:
          self.name = name
        if creation_time is not None:
          self.creation_time = creation_time
        if update_time is not None:
          self.update_time = update_time
        if deleted is not None:
          self.deleted = deleted
        if owner_name is not None:
          self.owner_name = owner_name
        if public is not None:
          self.public = public
        if togglable is not None:
          self.togglable = togglable
        if current_user_role_id is not None:
          self.current_user_role_id = current_user_role_id
        if repo_count is not None:
          self.repo_count = repo_count
        if enable_content_trust is not None:
          self.enable_content_trust = enable_content_trust
        if prevent_vulnerable_images_from_running is not None:
          self.prevent_vulnerable_images_from_running = prevent_vulnerable_images_from_running
        if prevent_vulnerable_images_from_running_severity is not None:
          self.prevent_vulnerable_images_from_running_severity = prevent_vulnerable_images_from_running_severity
        if automatically_scan_images_on_push is not None:
          self.automatically_scan_images_on_push = automatically_scan_images_on_push

    @property
    def project_id(self):
        """
        Gets the project_id of this Project.
        Project ID

        :return: The project_id of this Project.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Project.
        Project ID

        :param project_id: The project_id of this Project.
        :type: int
        """

        self._project_id = project_id

    @property
    def owner_id(self):
        """
        Gets the owner_id of this Project.
        The owner ID of the project always means the creator of the project.

        :return: The owner_id of this Project.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this Project.
        The owner ID of the project always means the creator of the project.

        :param owner_id: The owner_id of this Project.
        :type: int
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """
        Gets the name of this Project.
        The name of the project.

        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Project.
        The name of the project.

        :param name: The name of this Project.
        :type: str
        """

        self._name = name

    @property
    def creation_time(self):
        """
        Gets the creation_time of this Project.
        The creation time of the project.

        :return: The creation_time of this Project.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this Project.
        The creation time of the project.

        :param creation_time: The creation_time of this Project.
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """
        Gets the update_time of this Project.
        The update time of the project.

        :return: The update_time of this Project.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this Project.
        The update time of the project.

        :param update_time: The update_time of this Project.
        :type: str
        """

        self._update_time = update_time

    @property
    def deleted(self):
        """
        Gets the deleted of this Project.
        A deletion mark of the project (1 means it's deleted, 0 is not)

        :return: The deleted of this Project.
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this Project.
        A deletion mark of the project (1 means it's deleted, 0 is not)

        :param deleted: The deleted of this Project.
        :type: int
        """

        self._deleted = deleted

    @property
    def owner_name(self):
        """
        Gets the owner_name of this Project.
        The owner name of the project.

        :return: The owner_name of this Project.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """
        Sets the owner_name of this Project.
        The owner name of the project.

        :param owner_name: The owner_name of this Project.
        :type: str
        """

        self._owner_name = owner_name

    @property
    def public(self):
        """
        Gets the public of this Project.
        The public status of the project.

        :return: The public of this Project.
        :rtype: int
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this Project.
        The public status of the project.

        :param public: The public of this Project.
        :type: int
        """

        self._public = public

    @property
    def togglable(self):
        """
        Gets the togglable of this Project.
        Correspond to the UI about whether the project's publicity is  updatable (for UI)

        :return: The togglable of this Project.
        :rtype: bool
        """
        return self._togglable

    @togglable.setter
    def togglable(self, togglable):
        """
        Sets the togglable of this Project.
        Correspond to the UI about whether the project's publicity is  updatable (for UI)

        :param togglable: The togglable of this Project.
        :type: bool
        """

        self._togglable = togglable

    @property
    def current_user_role_id(self):
        """
        Gets the current_user_role_id of this Project.
        The role ID of the current user who triggered the API (for UI)

        :return: The current_user_role_id of this Project.
        :rtype: int
        """
        return self._current_user_role_id

    @current_user_role_id.setter
    def current_user_role_id(self, current_user_role_id):
        """
        Sets the current_user_role_id of this Project.
        The role ID of the current user who triggered the API (for UI)

        :param current_user_role_id: The current_user_role_id of this Project.
        :type: int
        """

        self._current_user_role_id = current_user_role_id

    @property
    def repo_count(self):
        """
        Gets the repo_count of this Project.
        The number of the repositories under this project.

        :return: The repo_count of this Project.
        :rtype: int
        """
        return self._repo_count

    @repo_count.setter
    def repo_count(self, repo_count):
        """
        Sets the repo_count of this Project.
        The number of the repositories under this project.

        :param repo_count: The repo_count of this Project.
        :type: int
        """

        self._repo_count = repo_count

    @property
    def enable_content_trust(self):
        """
        Gets the enable_content_trust of this Project.
        Whether content trust is enabled or not. If it is enabled, user cann't pull unsigned images from this project.

        :return: The enable_content_trust of this Project.
        :rtype: bool
        """
        return self._enable_content_trust

    @enable_content_trust.setter
    def enable_content_trust(self, enable_content_trust):
        """
        Sets the enable_content_trust of this Project.
        Whether content trust is enabled or not. If it is enabled, user cann't pull unsigned images from this project.

        :param enable_content_trust: The enable_content_trust of this Project.
        :type: bool
        """

        self._enable_content_trust = enable_content_trust

    @property
    def prevent_vulnerable_images_from_running(self):
        """
        Gets the prevent_vulnerable_images_from_running of this Project.
        Whether prevent the vulnerable images from running.

        :return: The prevent_vulnerable_images_from_running of this Project.
        :rtype: bool
        """
        return self._prevent_vulnerable_images_from_running

    @prevent_vulnerable_images_from_running.setter
    def prevent_vulnerable_images_from_running(self, prevent_vulnerable_images_from_running):
        """
        Sets the prevent_vulnerable_images_from_running of this Project.
        Whether prevent the vulnerable images from running.

        :param prevent_vulnerable_images_from_running: The prevent_vulnerable_images_from_running of this Project.
        :type: bool
        """

        self._prevent_vulnerable_images_from_running = prevent_vulnerable_images_from_running

    @property
    def prevent_vulnerable_images_from_running_severity(self):
        """
        Gets the prevent_vulnerable_images_from_running_severity of this Project.
        If the vulnerability is high than severity defined here, the images cann't be pulled.

        :return: The prevent_vulnerable_images_from_running_severity of this Project.
        :rtype: str
        """
        return self._prevent_vulnerable_images_from_running_severity

    @prevent_vulnerable_images_from_running_severity.setter
    def prevent_vulnerable_images_from_running_severity(self, prevent_vulnerable_images_from_running_severity):
        """
        Sets the prevent_vulnerable_images_from_running_severity of this Project.
        If the vulnerability is high than severity defined here, the images cann't be pulled.

        :param prevent_vulnerable_images_from_running_severity: The prevent_vulnerable_images_from_running_severity of this Project.
        :type: str
        """

        self._prevent_vulnerable_images_from_running_severity = prevent_vulnerable_images_from_running_severity

    @property
    def automatically_scan_images_on_push(self):
        """
        Gets the automatically_scan_images_on_push of this Project.
        Whether scan images automatically when pushing.

        :return: The automatically_scan_images_on_push of this Project.
        :rtype: bool
        """
        return self._automatically_scan_images_on_push

    @automatically_scan_images_on_push.setter
    def automatically_scan_images_on_push(self, automatically_scan_images_on_push):
        """
        Sets the automatically_scan_images_on_push of this Project.
        Whether scan images automatically when pushing.

        :param automatically_scan_images_on_push: The automatically_scan_images_on_push of this Project.
        :type: bool
        """

        self._automatically_scan_images_on_push = automatically_scan_images_on_push

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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
