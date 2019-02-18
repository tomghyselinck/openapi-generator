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

from petstore_api.utils import (
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    date,
    datetime,
    file_type,
    model_to_dict,
    none_type,
    validate_type
)
from petstore_api.models.outer_enum import OuterEnum


class EnumTest(object):
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
                            Optional, required variables, and
                            additional properties.
    """
    openapi_types = {
        'enum_string': (str,),
        'enum_string_required': (str,),
        'enum_integer': (int,),
        'enum_number': (float,),
        'outer_enum': (OuterEnum,)
    }
    attribute_map = {
        'enum_string': 'enum_string',
        'enum_string_required': 'enum_string_required',
        'enum_integer': 'enum_integer',
        'enum_number': 'enum_number',
        'outer_enum': 'outerEnum'
    }

    def __init__(self, enum_string_required, _check_type=False, **kwargs):  # noqa: E501
        """EnumTest - a model defined in OpenAPI

        Args:
            enum_string_required (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            enum_string (str): [optional]
            enum_integer (int): [optional]
            enum_number (float): [optional]
            outer_enum (OuterEnum): [optional]
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type

        # assign using .var_name to check against nullable and enums
        self.enum_string_required = enum_string_required
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
            raise ApiKeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        variable_path = [name]
        if not isinstance(name, str):
            raise ApiTypeError(
                (str,),
                name,
                variable_path,
                value_type=False
            )
        if check_type:
            validate_type(value, required_type, variable_path)

        self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]
        raise ApiKeyError("{0} has no key {1}".format(
            type(self).__name__, name))

    @property
    def enum_string(self):
        """Gets the enum_string of this EnumTest.  # noqa: E501


        Returns:
            str: The enum_string of this EnumTest.  # noqa: E501
        """
        return self._data_store.get('enum_string')

    @enum_string.setter
    def enum_string(self, enum_string):
        """Sets the enum_string of this EnumTest.


        Returns:
            str: The enum_string of this EnumTest.  # noqa: E501
        """
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if enum_string not in allowed_values:
            raise ApiValueError(
                "Invalid value for `enum_string` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string, allowed_values)
            )

        self.__setitem__('enum_string', enum_string)

    @property
    def enum_string_required(self):
        """Gets the enum_string_required of this EnumTest.  # noqa: E501


        Returns:
            str: The enum_string_required of this EnumTest.  # noqa: E501
        """
        return self._data_store.get('enum_string_required')

    @enum_string_required.setter
    def enum_string_required(self, enum_string_required):
        """Sets the enum_string_required of this EnumTest.


        Returns:
            str: The enum_string_required of this EnumTest.  # noqa: E501
        """
        if enum_string_required is None:
            raise ApiValueError("Invalid value for `enum_string_required`, must not be `None`")  # noqa: E501
        allowed_values = ["UPPER", "lower", ""]  # noqa: E501
        if enum_string_required not in allowed_values:
            raise ApiValueError(
                "Invalid value for `enum_string_required` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_string_required, allowed_values)
            )

        self.__setitem__('enum_string_required', enum_string_required)

    @property
    def enum_integer(self):
        """Gets the enum_integer of this EnumTest.  # noqa: E501


        Returns:
            int: The enum_integer of this EnumTest.  # noqa: E501
        """
        return self._data_store.get('enum_integer')

    @enum_integer.setter
    def enum_integer(self, enum_integer):
        """Sets the enum_integer of this EnumTest.


        Returns:
            int: The enum_integer of this EnumTest.  # noqa: E501
        """
        allowed_values = [1, -1]  # noqa: E501
        if enum_integer not in allowed_values:
            raise ApiValueError(
                "Invalid value for `enum_integer` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_integer, allowed_values)
            )

        self.__setitem__('enum_integer', enum_integer)

    @property
    def enum_number(self):
        """Gets the enum_number of this EnumTest.  # noqa: E501


        Returns:
            float: The enum_number of this EnumTest.  # noqa: E501
        """
        return self._data_store.get('enum_number')

    @enum_number.setter
    def enum_number(self, enum_number):
        """Sets the enum_number of this EnumTest.


        Returns:
            float: The enum_number of this EnumTest.  # noqa: E501
        """
        allowed_values = [1.1, -1.2]  # noqa: E501
        if enum_number not in allowed_values:
            raise ApiValueError(
                "Invalid value for `enum_number` ({0}), must be one of {1}"  # noqa: E501
                .format(enum_number, allowed_values)
            )

        self.__setitem__('enum_number', enum_number)

    @property
    def outer_enum(self):
        """Gets the outer_enum of this EnumTest.  # noqa: E501


        Returns:
            OuterEnum: The outer_enum of this EnumTest.  # noqa: E501
        """
        return self._data_store.get('outer_enum')

    @outer_enum.setter
    def outer_enum(self, outer_enum):
        """Sets the outer_enum of this EnumTest.


        Returns:
            OuterEnum: The outer_enum of this EnumTest.  # noqa: E501
        """

        self.__setitem__('outer_enum', outer_enum)

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

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
