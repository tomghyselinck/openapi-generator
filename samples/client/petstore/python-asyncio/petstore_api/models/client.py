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
    get_simple_class,
    int,
    model_to_dict,
    none_type,
    str,
    type_error_message,
    validate_and_convert_types
)


class Client(OpenApiModel):
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
        'client': [str]  # noqa: E501
    }
    attribute_map = {
        'client': 'client'  # noqa: E501
    }

    def __init__(self, _check_type=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """Client - a model defined in OpenAPI



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
            client (str): [optional]  # noqa: E501
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

        if get_simple_class(name) != str:
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
    def client(self):
        """Gets the client of this Client.  # noqa: E501


        Returns:
            (str): The client of this Client.  # noqa: E501
        """
        return self._data_store.get('client')

    @client.setter
    def client(
            self, client):
        """Sets the client of this Client.


        Returns:
            (str): The client of this Client.  # noqa: E501
        """

        self.__setitem__(
            'client',
            client
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
        if not isinstance(other, Client):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
