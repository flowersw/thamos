# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AdviseInput(object):
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
        'application_stack': 'object',
        'runtime_environment': 'object',
        'library_usage': 'object'
    }

    attribute_map = {
        'application_stack': 'application_stack',
        'runtime_environment': 'runtime_environment',
        'library_usage': 'library_usage'
    }

    def __init__(self, application_stack=None, runtime_environment=None, library_usage=None):  # noqa: E501
        """AdviseInput - a model defined in Swagger"""  # noqa: E501
        self._application_stack = None
        self._runtime_environment = None
        self._library_usage = None
        self.discriminator = None
        self.application_stack = application_stack
        if runtime_environment is not None:
            self.runtime_environment = runtime_environment
        if library_usage is not None:
            self.library_usage = library_usage

    @property
    def application_stack(self):
        """Gets the application_stack of this AdviseInput.  # noqa: E501


        :return: The application_stack of this AdviseInput.  # noqa: E501
        :rtype: object
        """
        return self._application_stack

    @application_stack.setter
    def application_stack(self, application_stack):
        """Sets the application_stack of this AdviseInput.


        :param application_stack: The application_stack of this AdviseInput.  # noqa: E501
        :type: object
        """
        if application_stack is None:
            raise ValueError("Invalid value for `application_stack`, must not be `None`")  # noqa: E501

        self._application_stack = application_stack

    @property
    def runtime_environment(self):
        """Gets the runtime_environment of this AdviseInput.  # noqa: E501


        :return: The runtime_environment of this AdviseInput.  # noqa: E501
        :rtype: object
        """
        return self._runtime_environment

    @runtime_environment.setter
    def runtime_environment(self, runtime_environment):
        """Sets the runtime_environment of this AdviseInput.


        :param runtime_environment: The runtime_environment of this AdviseInput.  # noqa: E501
        :type: object
        """

        self._runtime_environment = runtime_environment

    @property
    def library_usage(self):
        """Gets the library_usage of this AdviseInput.  # noqa: E501

        Static analysis of libraries used within user's project.  # noqa: E501

        :return: The library_usage of this AdviseInput.  # noqa: E501
        :rtype: object
        """
        return self._library_usage

    @library_usage.setter
    def library_usage(self, library_usage):
        """Sets the library_usage of this AdviseInput.

        Static analysis of libraries used within user's project.  # noqa: E501

        :param library_usage: The library_usage of this AdviseInput.  # noqa: E501
        :type: object
        """

        self._library_usage = library_usage

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
        if issubclass(AdviseInput, dict):
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
        if not isinstance(other, AdviseInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
