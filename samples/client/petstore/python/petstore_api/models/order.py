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


class Order(object):
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
        'id': (int,),
        'pet_id': (int,),
        'quantity': (int,),
        'ship_date': (datetime,),
        'status': (str,),
        'complete': (bool,)
    }
    attribute_map = {
        'id': 'id',
        'pet_id': 'petId',
        'quantity': 'quantity',
        'ship_date': 'shipDate',
        'status': 'status',
        'complete': 'complete'
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """Order - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            id (int): [optional]
            pet_id (int): [optional]
            quantity (int): [optional]
            ship_date (datetime): [optional]
            status (str): Order Status. [optional]
            complete (bool): [optional] if omitted the server will use the default value of False
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
    def id(self):
        """Gets the id of this Order.  # noqa: E501


        Returns:
            int: The id of this Order.  # noqa: E501
        """
        return self._data_store.get('id')

    @id.setter
    def id(self, id):
        """Sets the id of this Order.


        Returns:
            int: The id of this Order.  # noqa: E501
        """

        self.__setitem__('id', id)

    @property
    def pet_id(self):
        """Gets the pet_id of this Order.  # noqa: E501


        Returns:
            int: The pet_id of this Order.  # noqa: E501
        """
        return self._data_store.get('pet_id')

    @pet_id.setter
    def pet_id(self, pet_id):
        """Sets the pet_id of this Order.


        Returns:
            int: The pet_id of this Order.  # noqa: E501
        """

        self.__setitem__('pet_id', pet_id)

    @property
    def quantity(self):
        """Gets the quantity of this Order.  # noqa: E501


        Returns:
            int: The quantity of this Order.  # noqa: E501
        """
        return self._data_store.get('quantity')

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.


        Returns:
            int: The quantity of this Order.  # noqa: E501
        """

        self.__setitem__('quantity', quantity)

    @property
    def ship_date(self):
        """Gets the ship_date of this Order.  # noqa: E501


        Returns:
            datetime: The ship_date of this Order.  # noqa: E501
        """
        return self._data_store.get('ship_date')

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this Order.


        Returns:
            datetime: The ship_date of this Order.  # noqa: E501
        """

        self.__setitem__('ship_date', ship_date)

    @property
    def status(self):
        """Gets the status of this Order.  # noqa: E501

        Order Status  # noqa: E501

        Returns:
            str: The status of this Order.  # noqa: E501
        """
        return self._data_store.get('status')

    @status.setter
    def status(self, status):
        """Sets the status of this Order.

        Order Status  # noqa: E501

        Returns:
            str: The status of this Order.  # noqa: E501
        """
        allowed_values = ["placed", "approved", "delivered"]  # noqa: E501
        if status not in allowed_values:
            raise ApiValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self.__setitem__('status', status)

    @property
    def complete(self):
        """Gets the complete of this Order.  # noqa: E501


        Returns:
            bool: The complete of this Order.  # noqa: E501
        """
        return self._data_store.get('complete')

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this Order.


        Returns:
            bool: The complete of this Order.  # noqa: E501
        """

        self.__setitem__('complete', complete)

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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
