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

from petstore_api.exceptions import (
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
)
from petstore_api.model_utils import (  # noqa: F401
    OpenApiModel,
    date,
    datetime,
    file_type,
    model_to_dict,
    none_type,
    validate_type
)


class EnumArrays(OpenApiModel):
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
        'just_symbol': [str],  # noqa: E501
        'array_enum': [[(str,)]]  # noqa: E501
    }
    attribute_map = {
        'just_symbol': 'just_symbol',  # noqa: E501
        'array_enum': 'array_enum'  # noqa: E501
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """EnumArrays - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            just_symbol (str): [optional]  # noqa: E501
            array_enum ([(str,)]): [optional]  # noqa: E501
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
    def just_symbol(self):
        """Gets the just_symbol of this EnumArrays.  # noqa: E501


        Returns:
            (str): The just_symbol of this EnumArrays.  # noqa: E501
        """
        return self._data_store.get('just_symbol')

    @just_symbol.setter
    def just_symbol(
            self, just_symbol):
        """Sets the just_symbol of this EnumArrays.


        Returns:
            (str): The just_symbol of this EnumArrays.  # noqa: E501
        """
        allowed_values = [">=", "$"]  # noqa: E501
        if just_symbol not in allowed_values:
            raise ApiValueError(
                "Invalid value for `just_symbol` ({0}), must be one of {1}"  # noqa: E501
                .format(just_symbol, allowed_values)
            )

        self.__setitem__(
            'just_symbol',
            just_symbol
        )

    @property
    def array_enum(self):
        """Gets the array_enum of this EnumArrays.  # noqa: E501


        Returns:
            ([(str,)]): The array_enum of this EnumArrays.  # noqa: E501
        """
        return self._data_store.get('array_enum')

    @array_enum.setter
    def array_enum(
            self, array_enum):
        """Sets the array_enum of this EnumArrays.


        Returns:
            ([(str,)]): The array_enum of this EnumArrays.  # noqa: E501
        """
        allowed_values = ["fish", "crab"]  # noqa: E501
        if not set(array_enum).issubset(set(allowed_values)):
            raise ApiValueError(
                "Invalid values for `array_enum` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(array_enum) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self.__setitem__(
            'array_enum',
            array_enum
        )

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
        if not isinstance(other, EnumArrays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
