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
    type_error_message,
    validate_and_convert_types
)


class MapTest(OpenApiModel):
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
        'map_map_of_string': [{str: ({str: (str,)},)}],  # noqa: E501
        'map_of_enum_string': [{str: (str,)}],  # noqa: E501
        'direct_map': [{str: (bool,)}],  # noqa: E501
        'indirect_map': [{str: (bool,)}]  # noqa: E501
    }
    attribute_map = {
        'map_map_of_string': 'map_map_of_string',  # noqa: E501
        'map_of_enum_string': 'map_of_enum_string',  # noqa: E501
        'direct_map': 'direct_map',  # noqa: E501
        'indirect_map': 'indirect_map'  # noqa: E501
    }

    def __init__(self, _check_type=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """MapTest - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            map_map_of_string ({str: ({str: (str,)},)}): [optional]  # noqa: E501
            map_of_enum_string ({str: (str,)}): [optional]  # noqa: E501
            direct_map ({str: (bool,)}): [optional]  # noqa: E501
            indirect_map ({str: (bool,)}): [optional]  # noqa: E501
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            if var_name in self.openapi_types:
                # assign using .var_name to check against nullable and enums
                setattr(self, var_name, var_value)
            else:
                self.__setitem__(var_name, var_value)

    def __setitem__(self, name, value):
        if name in self.openapi_types:
            check_type = self._check_type
            required_types_mixed = self.openapi_types[name]
        else:
            path_to_item = []
            if self._path_to_item:
                path_to_item.extend(self._path_to_item)
            path_to_item.append(name)
            raise ApiKeyError(
                "{0} has no key '{1}'".format(type(self).__name__, name),
                path_to_item
            )

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)

        if not isinstance(name, str):
            error_msg = type_error_message(
                var_name=name,
                var_value=name,
                valid_classes=(str,),
                key_type=True
            )
            raise ApiTypeError(
                error_msg,
                path_to_item=path_to_item,
                valid_classes=(str,),
                key_type=True
            )

        if check_type:
            self._data_store[name] = validate_and_convert_types(
                value, required_types_mixed, path_to_item,
                configuration=self._configuration)
        else:
            self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)
        raise ApiKeyError(
            "{0} has no key '{1}'".format(type(self).__name__, name),
            [name]
        )

    @property
    def map_map_of_string(self):
        """Gets the map_map_of_string of this MapTest.  # noqa: E501


        Returns:
            ({str: ({str: (str,)},)}): The map_map_of_string of this MapTest.  # noqa: E501
        """
        return self._data_store.get('map_map_of_string')

    @map_map_of_string.setter
    def map_map_of_string(
            self, map_map_of_string):
        """Sets the map_map_of_string of this MapTest.


        Returns:
            ({str: ({str: (str,)},)}): The map_map_of_string of this MapTest.  # noqa: E501
        """

        self.__setitem__(
            'map_map_of_string',
            map_map_of_string
        )

    @property
    def map_of_enum_string(self):
        """Gets the map_of_enum_string of this MapTest.  # noqa: E501


        Returns:
            ({str: (str,)}): The map_of_enum_string of this MapTest.  # noqa: E501
        """
        return self._data_store.get('map_of_enum_string')

    @map_of_enum_string.setter
    def map_of_enum_string(
            self, map_of_enum_string):
        """Sets the map_of_enum_string of this MapTest.


        Returns:
            ({str: (str,)}): The map_of_enum_string of this MapTest.  # noqa: E501
        """
        allowed_values = ["UPPER", "lower"]  # noqa: E501
        if not set(map_of_enum_string.keys()).issubset(set(allowed_values)):
            raise ApiValueError(
                "Invalid keys in `map_of_enum_string` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(map_of_enum_string.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self.__setitem__(
            'map_of_enum_string',
            map_of_enum_string
        )

    @property
    def direct_map(self):
        """Gets the direct_map of this MapTest.  # noqa: E501


        Returns:
            ({str: (bool,)}): The direct_map of this MapTest.  # noqa: E501
        """
        return self._data_store.get('direct_map')

    @direct_map.setter
    def direct_map(
            self, direct_map):
        """Sets the direct_map of this MapTest.


        Returns:
            ({str: (bool,)}): The direct_map of this MapTest.  # noqa: E501
        """

        self.__setitem__(
            'direct_map',
            direct_map
        )

    @property
    def indirect_map(self):
        """Gets the indirect_map of this MapTest.  # noqa: E501


        Returns:
            ({str: (bool,)}): The indirect_map of this MapTest.  # noqa: E501
        """
        return self._data_store.get('indirect_map')

    @indirect_map.setter
    def indirect_map(
            self, indirect_map):
        """Sets the indirect_map of this MapTest.


        Returns:
            ({str: (bool,)}): The indirect_map of this MapTest.  # noqa: E501
        """

        self.__setitem__(
            'indirect_map',
            indirect_map
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
        if not isinstance(other, MapTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
