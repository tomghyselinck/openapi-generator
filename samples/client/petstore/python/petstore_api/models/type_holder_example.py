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


class TypeHolderExample(object):
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
        'string_item': 'str',
        'number_item': 'float',
        'integer_item': 'int',
        'bool_item': 'bool',
        'array_item': 'list[int]'
    }
    attribute_map = {
        'string_item': 'string_item',
        'number_item': 'number_item',
        'integer_item': 'integer_item',
        'bool_item': 'bool_item',
        'array_item': 'array_item'
    }

    def __init__(self, string_item='what', number_item=1.234, integer_item=-2, bool_item=True, array_item=[0, 1, 2, 3], _check_type=False, **kwargs):  # noqa: E501
        """TypeHolderExample - a model defined in OpenAPI

        Args:
            string_item (str): defaults to 'what', must be one of ['what']
            number_item (float): defaults to 1.234, must be one of [1.234]
            integer_item (int): defaults to -2, must be one of [-2]
            bool_item (bool): defaults to True, must be one of [True]
            array_item (list[int]): defaults to [0, 1, 2, 3], must be one of [[0, 1, 2, 3]]

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type

        # assign using .var_name to check against nullable and enums
        self.string_item = string_item
        self.number_item = number_item
        self.integer_item = integer_item
        self.bool_item = bool_item
        self.array_item = array_item
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
    def string_item(self):
        """Gets the string_item of this TypeHolderExample.  # noqa: E501


        :return: The string_item of this TypeHolderExample.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('string_item')

    @string_item.setter
    def string_item(self, string_item):
        """Sets the string_item of this TypeHolderExample.


        :param string_item: The string_item of this TypeHolderExample.  # noqa: E501
        :type: str
        """
        if string_item is None:
            raise ValueError("Invalid value for `string_item`, must not be `None`")  # noqa: E501

        self.__setitem__('string_item', string_item)

    @property
    def number_item(self):
        """Gets the number_item of this TypeHolderExample.  # noqa: E501


        :return: The number_item of this TypeHolderExample.  # noqa: E501
        :rtype: float
        """
        return self._data_store.get('number_item')

    @number_item.setter
    def number_item(self, number_item):
        """Sets the number_item of this TypeHolderExample.


        :param number_item: The number_item of this TypeHolderExample.  # noqa: E501
        :type: float
        """
        if number_item is None:
            raise ValueError("Invalid value for `number_item`, must not be `None`")  # noqa: E501

        self.__setitem__('number_item', number_item)

    @property
    def integer_item(self):
        """Gets the integer_item of this TypeHolderExample.  # noqa: E501


        :return: The integer_item of this TypeHolderExample.  # noqa: E501
        :rtype: int
        """
        return self._data_store.get('integer_item')

    @integer_item.setter
    def integer_item(self, integer_item):
        """Sets the integer_item of this TypeHolderExample.


        :param integer_item: The integer_item of this TypeHolderExample.  # noqa: E501
        :type: int
        """
        if integer_item is None:
            raise ValueError("Invalid value for `integer_item`, must not be `None`")  # noqa: E501

        self.__setitem__('integer_item', integer_item)

    @property
    def bool_item(self):
        """Gets the bool_item of this TypeHolderExample.  # noqa: E501


        :return: The bool_item of this TypeHolderExample.  # noqa: E501
        :rtype: bool
        """
        return self._data_store.get('bool_item')

    @bool_item.setter
    def bool_item(self, bool_item):
        """Sets the bool_item of this TypeHolderExample.


        :param bool_item: The bool_item of this TypeHolderExample.  # noqa: E501
        :type: bool
        """
        if bool_item is None:
            raise ValueError("Invalid value for `bool_item`, must not be `None`")  # noqa: E501

        self.__setitem__('bool_item', bool_item)

    @property
    def array_item(self):
        """Gets the array_item of this TypeHolderExample.  # noqa: E501


        :return: The array_item of this TypeHolderExample.  # noqa: E501
        :rtype: list[int]
        """
        return self._data_store.get('array_item')

    @array_item.setter
    def array_item(self, array_item):
        """Sets the array_item of this TypeHolderExample.


        :param array_item: The array_item of this TypeHolderExample.  # noqa: E501
        :type: list[int]
        """
        if array_item is None:
            raise ValueError("Invalid value for `array_item`, must not be `None`")  # noqa: E501

        self.__setitem__('array_item', array_item)

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
        if not isinstance(other, TypeHolderExample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
