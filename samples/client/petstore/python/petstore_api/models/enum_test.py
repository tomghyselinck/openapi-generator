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


class EnumTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'enum_string': 'str',
        'enum_string_required': 'str',
        'enum_integer': 'int',
        'enum_number': 'float',
        'outer_enum': 'OuterEnum'
    }
    attribute_map = {
        'enum_string': 'enum_string',
        'enum_string_required': 'enum_string_required',
        'enum_integer': 'enum_integer',
        'enum_number': 'enum_number',
        'outer_enum': 'outerEnum'
    }

    def __init__(self, enum_string_required, **kwargs):  # noqa: E501
        """EnumTest - a model defined in OpenAPI"""  # noqa: E501

        self._data_store = {}

        self.discriminator = None
        self.__setitem__('enum_string_required', enum_string_required)

        for var_name, var_value in six.iteritems(kwargs):
            self.__setitem__(var_name, var_value)

    def recursive_type(self, item):
        """Gets a string describing the full the recursive type of a value"""
        item_type = type(item)
        if item_type == dict:
            child_key_types = set()
            child_value_types = set()
            for child_key, child_value in six.iteritems(item):
                child_key_types.add(self.recursive_type(child_key))
                child_value_types.add(self.recursive_type(child_value))
            if child_key_types != set(['str']):
                raise ValueError('Invalid dict key type. All Openapi dict keys must be strings')
            child_value_types = '|'.join(sorted(list(child_value_types)))
            return "dict(str, {0})".format(child_value_types)
        elif item_type == list:
            child_value_types = set()
            for child_item in item:
                child_value_types.add(self.recursive_type(child_item))
            child_value_types = '|'.join(sorted(list(child_value_types)))
            return "list[{0}]".format(child_value_types)
        else:
            return type(item).__name__

    def __setitem__(self, name, value):
        check_type = False
        if name in self.openapi_types:
            required_type = self.openapi_types[name]
        else:
            raise KeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        passed_type = self.recursive_type(value)
        if type(name) != str:
            raise ValueError('Variable name must be type string and %s was not' % name)
        elif passed_type != required_type and check_type:
            raise ValueError('Variable value must be type %s but you passed in %s' %
                             (required_type, passed_type))

        if name in self.openapi_types:
            setattr(self, name, value)
        else:
            self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]
        raise KeyError("{0} has no key {1}".format(
            type(self).__name__, name))

    @property
    def enum_string(self):
        """Gets the enum_string of this EnumTest.  # noqa: E501


        :return: The enum_string of this EnumTest.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('enum_string')

    @enum_string.setter
    def enum_string(self, enum_string):
        """Sets the enum_string of this EnumTest.


        :param enum_string: The enum_string of this EnumTest.  # noqa: E501
        :type: str
        """
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if enum_string not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_string` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string, allowed_values)
            )

        self._data_store['enum_string'] = enum_string

    @property
    def enum_string_required(self):
        """Gets the enum_string_required of this EnumTest.  # noqa: E501


        :return: The enum_string_required of this EnumTest.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('enum_string_required')

    @enum_string_required.setter
    def enum_string_required(self, enum_string_required):
        """Sets the enum_string_required of this EnumTest.


        :param enum_string_required: The enum_string_required of this EnumTest.  # noqa: E501
        :type: str
        """
        if enum_string_required is None:
            raise ValueError("Invalid value for `enum_string_required`, must not be `None`")  # noqa: E501
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if enum_string_required not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_string_required` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string_required, allowed_values)
            )

        self._data_store['enum_string_required'] = enum_string_required

    @property
    def enum_integer(self):
        """Gets the enum_integer of this EnumTest.  # noqa: E501


        :return: The enum_integer of this EnumTest.  # noqa: E501
        :rtype: int
        """
        return self._data_store.get('enum_integer')

    @enum_integer.setter
    def enum_integer(self, enum_integer):
        """Sets the enum_integer of this EnumTest.


        :param enum_integer: The enum_integer of this EnumTest.  # noqa: E501
        :type: int
        """
        allowed_values = [1, -1]  # noqa: E501
        if enum_integer not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_integer` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_integer, allowed_values)
            )

        self._data_store['enum_integer'] = enum_integer

    @property
    def enum_number(self):
        """Gets the enum_number of this EnumTest.  # noqa: E501


        :return: The enum_number of this EnumTest.  # noqa: E501
        :rtype: float
        """
        return self._data_store.get('enum_number')

    @enum_number.setter
    def enum_number(self, enum_number):
        """Sets the enum_number of this EnumTest.


        :param enum_number: The enum_number of this EnumTest.  # noqa: E501
        :type: float
        """
        allowed_values = [1.1, -1.2]  # noqa: E501
        if enum_number not in allowed_values:
            raise ValueError(
                "Invalid value for `enum_number` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_number, allowed_values)
            )

        self._data_store['enum_number'] = enum_number

    @property
    def outer_enum(self):
        """Gets the outer_enum of this EnumTest.  # noqa: E501


        :return: The outer_enum of this EnumTest.  # noqa: E501
        :rtype: OuterEnum
        """
        return self._data_store.get('outer_enum')

    @outer_enum.setter
    def outer_enum(self, outer_enum):
        """Sets the outer_enum of this EnumTest.


        :param outer_enum: The outer_enum of this EnumTest.  # noqa: E501
        :type: OuterEnum
        """

        self._data_store['outer_enum'] = outer_enum

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
        if not isinstance(other, EnumTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
