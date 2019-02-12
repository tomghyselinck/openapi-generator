# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from petstore_api.utils import recursive_type, valid_type


class ApiResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
                            Optional and required variables only.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
                            Optional and required variables only.
    """
    openapi_types = {
        'code': 'int',
        'type': 'str',
        'message': 'str'
    }
    attribute_map = {
        'code': 'code',
        'type': 'type',
        'message': 'message'
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """ApiResponse - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            code (int): [optional]
            type (str): [optional]
            message (str): [optional]
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type

        for var_name, var_value in six.iteritems(kwargs):
            if var_name in self.openapi_types:
                # assign using .var_name to check against nullable and enums
                setattr(self, var_name, var_value)
            else:
                self.__setitem__(var_name, var_value)

    def __setitem__(self, name, value):
        if name in self.openapi_types:
            check_type = self._check_type
            required_type = self.openapi_types[name]
        else:
            raise KeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        passed_type = recursive_type(value)
        if type(name) != str:
            raise TypeError('Variable name must be type string and %s was not' % name)
        elif check_type and not valid_type(passed_type, required_type):
            raise TypeError('Variable value must be type %s but you passed in %s' %
                            (required_type, passed_type))

        self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]
        raise KeyError("{0} has no key {1}".format(
            type(self).__name__, name))

    @property
    def code(self):
        """Gets the code of this ApiResponse.  # noqa: E501


        :return: The code of this ApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._data_store.get('code')

    @code.setter
    def code(self, code):
        """Sets the code of this ApiResponse.


        :param code: The code of this ApiResponse.  # noqa: E501
        :type: int
        """

        self.__setitem__('code', code)

    @property
    def type(self):
        """Gets the type of this ApiResponse.  # noqa: E501


        :return: The type of this ApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('type')

    @type.setter
    def type(self, type):
        """Sets the type of this ApiResponse.


        :param type: The type of this ApiResponse.  # noqa: E501
        :type: str
        """

        self.__setitem__('type', type)

    @property
    def message(self):
        """Gets the message of this ApiResponse.  # noqa: E501


        :return: The message of this ApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('message')

    @message.setter
    def message(self, message):
        """Sets the message of this ApiResponse.


        :param message: The message of this ApiResponse.  # noqa: E501
        :type: str
        """

        self.__setitem__('message', message)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, value in six.iteritems(self._data_store):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
