# coding: utf-8

"""
    Thoth user API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RuntimeEnvironment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'hardware': 'object',
        'operating_system': 'object',
        'python_version': 'str',
        'cuda_version': 'str',
        'name': 'str'
    }

    attribute_map = {
        'hardware': 'hardware',
        'operating_system': 'operating_system',
        'python_version': 'python_version',
        'cuda_version': 'cuda_version',
        'name': 'name'
    }

    def __init__(self, hardware=None, operating_system=None, python_version=None, cuda_version=None, name=None):  # noqa: E501
        """RuntimeEnvironment - a model defined in Swagger"""  # noqa: E501

        self._hardware = None
        self._operating_system = None
        self._python_version = None
        self._cuda_version = None
        self._name = None
        self.discriminator = None

        if hardware is not None:
            self.hardware = hardware
        if operating_system is not None:
            self.operating_system = operating_system
        if python_version is not None:
            self.python_version = python_version
        if cuda_version is not None:
            self.cuda_version = cuda_version
        if name is not None:
            self.name = name

    @property
    def hardware(self):
        """Gets the hardware of this RuntimeEnvironment.  # noqa: E501


        :return: The hardware of this RuntimeEnvironment.  # noqa: E501
        :rtype: object
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this RuntimeEnvironment.


        :param hardware: The hardware of this RuntimeEnvironment.  # noqa: E501
        :type: object
        """

        self._hardware = hardware

    @property
    def operating_system(self):
        """Gets the operating_system of this RuntimeEnvironment.  # noqa: E501


        :return: The operating_system of this RuntimeEnvironment.  # noqa: E501
        :rtype: object
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this RuntimeEnvironment.


        :param operating_system: The operating_system of this RuntimeEnvironment.  # noqa: E501
        :type: object
        """

        self._operating_system = operating_system

    @property
    def python_version(self):
        """Gets the python_version of this RuntimeEnvironment.  # noqa: E501


        :return: The python_version of this RuntimeEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this RuntimeEnvironment.


        :param python_version: The python_version of this RuntimeEnvironment.  # noqa: E501
        :type: str
        """

        self._python_version = python_version

    @property
    def cuda_version(self):
        """Gets the cuda_version of this RuntimeEnvironment.  # noqa: E501


        :return: The cuda_version of this RuntimeEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._cuda_version

    @cuda_version.setter
    def cuda_version(self, cuda_version):
        """Sets the cuda_version of this RuntimeEnvironment.


        :param cuda_version: The cuda_version of this RuntimeEnvironment.  # noqa: E501
        :type: str
        """

        self._cuda_version = cuda_version

    @property
    def name(self):
        """Gets the name of this RuntimeEnvironment.  # noqa: E501


        :return: The name of this RuntimeEnvironment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuntimeEnvironment.


        :param name: The name of this RuntimeEnvironment.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RuntimeEnvironment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuntimeEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
