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


class Capitalization(OpenApiModel):
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
        'small_camel': [str],  # noqa: E501
        'capital_camel': [str],  # noqa: E501
        'small_snake': [str],  # noqa: E501
        'capital_snake': [str],  # noqa: E501
        'sca_eth_flow_points': [str],  # noqa: E501
        'att_name': [str]  # noqa: E501
    }
    attribute_map = {
        'small_camel': 'smallCamel',  # noqa: E501
        'capital_camel': 'CapitalCamel',  # noqa: E501
        'small_snake': 'small_Snake',  # noqa: E501
        'capital_snake': 'Capital_Snake',  # noqa: E501
        'sca_eth_flow_points': 'SCA_ETH_Flow_Points',  # noqa: E501
        'att_name': 'ATT_NAME'  # noqa: E501
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """Capitalization - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            small_camel (str): [optional]  # noqa: E501
            capital_camel (str): [optional]  # noqa: E501
            small_snake (str): [optional]  # noqa: E501
            capital_snake (str): [optional]  # noqa: E501
            sca_eth_flow_points (str): [optional]  # noqa: E501
            att_name (str): Name of the pet . [optional]  # noqa: E501
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
    def small_camel(self):
        """Gets the small_camel of this Capitalization.  # noqa: E501


        Returns:
            (str): The small_camel of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('small_camel')

    @small_camel.setter
    def small_camel(
            self, small_camel):
        """Sets the small_camel of this Capitalization.


        Returns:
            (str): The small_camel of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'small_camel',
            small_camel
        )

    @property
    def capital_camel(self):
        """Gets the capital_camel of this Capitalization.  # noqa: E501


        Returns:
            (str): The capital_camel of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('capital_camel')

    @capital_camel.setter
    def capital_camel(
            self, capital_camel):
        """Sets the capital_camel of this Capitalization.


        Returns:
            (str): The capital_camel of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'capital_camel',
            capital_camel
        )

    @property
    def small_snake(self):
        """Gets the small_snake of this Capitalization.  # noqa: E501


        Returns:
            (str): The small_snake of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('small_snake')

    @small_snake.setter
    def small_snake(
            self, small_snake):
        """Sets the small_snake of this Capitalization.


        Returns:
            (str): The small_snake of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'small_snake',
            small_snake
        )

    @property
    def capital_snake(self):
        """Gets the capital_snake of this Capitalization.  # noqa: E501


        Returns:
            (str): The capital_snake of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('capital_snake')

    @capital_snake.setter
    def capital_snake(
            self, capital_snake):
        """Sets the capital_snake of this Capitalization.


        Returns:
            (str): The capital_snake of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'capital_snake',
            capital_snake
        )

    @property
    def sca_eth_flow_points(self):
        """Gets the sca_eth_flow_points of this Capitalization.  # noqa: E501


        Returns:
            (str): The sca_eth_flow_points of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('sca_eth_flow_points')

    @sca_eth_flow_points.setter
    def sca_eth_flow_points(
            self, sca_eth_flow_points):
        """Sets the sca_eth_flow_points of this Capitalization.


        Returns:
            (str): The sca_eth_flow_points of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'sca_eth_flow_points',
            sca_eth_flow_points
        )

    @property
    def att_name(self):
        """Gets the att_name of this Capitalization.  # noqa: E501

        Name of the pet   # noqa: E501

        Returns:
            (str): The att_name of this Capitalization.  # noqa: E501
        """
        return self._data_store.get('att_name')

    @att_name.setter
    def att_name(
            self, att_name):
        """Sets the att_name of this Capitalization.

        Name of the pet   # noqa: E501

        Returns:
            (str): The att_name of this Capitalization.  # noqa: E501
        """

        self.__setitem__(
            'att_name',
            att_name
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
        if not isinstance(other, Capitalization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
