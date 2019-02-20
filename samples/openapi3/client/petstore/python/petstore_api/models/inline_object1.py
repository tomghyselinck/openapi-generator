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
    date,
    datetime,
    file_type,
    model_to_dict,
    none_type,
    validate_type
)


class InlineObject1(object):
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
        'additional_metadata': [str],  # noqa: E501
        'file': [file_type]  # noqa: E501
    }
    attribute_map = {
        'additional_metadata': 'additionalMetadata',  # noqa: E501
        'file': 'file'  # noqa: E501
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """InlineObject1 - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            additional_metadata (str): Additional data to pass to server. [optional]  # noqa: E501
            file (file_type): file to upload. [optional]  # noqa: E501
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
    def additional_metadata(self):
        """Gets the additional_metadata of this InlineObject1.  # noqa: E501

        Additional data to pass to server  # noqa: E501

        Returns:
            (str): The additional_metadata of this InlineObject1.  # noqa: E501
        """
        return self._data_store.get('additional_metadata')

    @additional_metadata.setter
    def additional_metadata(
            self, additional_metadata):
        """Sets the additional_metadata of this InlineObject1.

        Additional data to pass to server  # noqa: E501

        Returns:
            (str): The additional_metadata of this InlineObject1.  # noqa: E501
        """

        self.__setitem__(
            'additional_metadata',
            additional_metadata
        )

    @property
    def file(self):
        """Gets the file of this InlineObject1.  # noqa: E501

        file to upload  # noqa: E501

        Returns:
            (file_type): The file of this InlineObject1.  # noqa: E501
        """
        return self._data_store.get('file')

    @file.setter
    def file(
            self, file):
        """Sets the file of this InlineObject1.

        file to upload  # noqa: E501

        Returns:
            (file_type): The file of this InlineObject1.  # noqa: E501
        """

        self.__setitem__(
            'file',
            file
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
        if not isinstance(other, InlineObject1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
