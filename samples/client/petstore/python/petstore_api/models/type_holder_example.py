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

from petstore_api.utils import (  # noqa: F401
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiModel,
    date,
    datetime,
    file_type,
    model_to_dict,
    none_type,
    validate_type
)


class TypeHolderExample(OpenApiModel):
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
        'string_item': [str],  # noqa: E501
        'number_item': [float],  # noqa: E501
        'integer_item': [int],  # noqa: E501
        'bool_item': [bool],  # noqa: E501
        'array_item': [[(int,)]]  # noqa: E501
    }
    attribute_map = {
        'string_item': 'string_item',  # noqa: E501
        'number_item': 'number_item',  # noqa: E501
        'integer_item': 'integer_item',  # noqa: E501
        'bool_item': 'bool_item',  # noqa: E501
        'array_item': 'array_item'  # noqa: E501
    }

    def __init__(self, string_item='what', number_item=1.234, integer_item=-2, bool_item=True, array_item=[0, 1, 2, 3], _check_type=False, **kwargs):  # noqa: E501
        """TypeHolderExample - a model defined in OpenAPI

        Args:
            string_item (str): defaults to 'what', must be one of ['what']  # noqa: E501
            number_item (float): defaults to 1.234, must be one of [1.234]  # noqa: E501
            integer_item (int): defaults to -2, must be one of [-2]  # noqa: E501
            bool_item (bool): defaults to True, must be one of [True]  # noqa: E501
            array_item ([(int,)]): defaults to [0, 1, 2, 3], must be one of [[0, 1, 2, 3]]  # noqa: E501

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
    def string_item(self):
        """Gets the string_item of this TypeHolderExample.  # noqa: E501


        Returns:
            (str): The string_item of this TypeHolderExample.  # noqa: E501
        """
        return self._data_store.get('string_item')

    @string_item.setter
    def string_item(
            self, string_item):
        """Sets the string_item of this TypeHolderExample.


        Returns:
            (str): The string_item of this TypeHolderExample.  # noqa: E501
        """
        if string_item is None:
            raise ApiValueError("Invalid value for `string_item`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'string_item',
            string_item
        )

    @property
    def number_item(self):
        """Gets the number_item of this TypeHolderExample.  # noqa: E501


        Returns:
            (float): The number_item of this TypeHolderExample.  # noqa: E501
        """
        return self._data_store.get('number_item')

    @number_item.setter
    def number_item(
            self, number_item):
        """Sets the number_item of this TypeHolderExample.


        Returns:
            (float): The number_item of this TypeHolderExample.  # noqa: E501
        """
        if number_item is None:
            raise ApiValueError("Invalid value for `number_item`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'number_item',
            number_item
        )

    @property
    def integer_item(self):
        """Gets the integer_item of this TypeHolderExample.  # noqa: E501


        Returns:
            (int): The integer_item of this TypeHolderExample.  # noqa: E501
        """
        return self._data_store.get('integer_item')

    @integer_item.setter
    def integer_item(
            self, integer_item):
        """Sets the integer_item of this TypeHolderExample.


        Returns:
            (int): The integer_item of this TypeHolderExample.  # noqa: E501
        """
        if integer_item is None:
            raise ApiValueError("Invalid value for `integer_item`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'integer_item',
            integer_item
        )

    @property
    def bool_item(self):
        """Gets the bool_item of this TypeHolderExample.  # noqa: E501


        Returns:
            (bool): The bool_item of this TypeHolderExample.  # noqa: E501
        """
        return self._data_store.get('bool_item')

    @bool_item.setter
    def bool_item(
            self, bool_item):
        """Sets the bool_item of this TypeHolderExample.


        Returns:
            (bool): The bool_item of this TypeHolderExample.  # noqa: E501
        """
        if bool_item is None:
            raise ApiValueError("Invalid value for `bool_item`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'bool_item',
            bool_item
        )

    @property
    def array_item(self):
        """Gets the array_item of this TypeHolderExample.  # noqa: E501


        Returns:
            ([(int,)]): The array_item of this TypeHolderExample.  # noqa: E501
        """
        return self._data_store.get('array_item')

    @array_item.setter
    def array_item(
            self, array_item):
        """Sets the array_item of this TypeHolderExample.


        Returns:
            ([(int,)]): The array_item of this TypeHolderExample.  # noqa: E501
        """
        if array_item is None:
            raise ApiValueError("Invalid value for `array_item`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'array_item',
            array_item
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
        if not isinstance(other, TypeHolderExample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
