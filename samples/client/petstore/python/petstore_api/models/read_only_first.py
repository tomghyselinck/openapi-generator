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


class ReadOnlyFirst(object):
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
        'bar': (str,),
        'baz': (str,)
    }
    attribute_map = {
        'bar': 'bar',
        'baz': 'baz'
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """ReadOnlyFirst - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            bar (str): [optional]
            baz (str): [optional]
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
    def bar(self):
        """Gets the bar of this ReadOnlyFirst.  # noqa: E501


        Returns:
            str: The bar of this ReadOnlyFirst.  # noqa: E501
        """
        return self._data_store.get('bar')

    @bar.setter
    def bar(self, bar):
        """Sets the bar of this ReadOnlyFirst.


        Returns:
            str: The bar of this ReadOnlyFirst.  # noqa: E501
        """

        self.__setitem__('bar', bar)

    @property
    def baz(self):
        """Gets the baz of this ReadOnlyFirst.  # noqa: E501


        Returns:
            str: The baz of this ReadOnlyFirst.  # noqa: E501
        """
        return self._data_store.get('baz')

    @baz.setter
    def baz(self, baz):
        """Sets the baz of this ReadOnlyFirst.


        Returns:
            str: The baz of this ReadOnlyFirst.  # noqa: E501
        """

        self.__setitem__('baz', baz)

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
        if not isinstance(other, ReadOnlyFirst):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
