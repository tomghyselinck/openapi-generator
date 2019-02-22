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


class XmlItem(OpenApiModel):
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
        'attribute_string': [str],  # noqa: E501
        'attribute_number': [float],  # noqa: E501
        'attribute_integer': [int],  # noqa: E501
        'attribute_boolean': [bool],  # noqa: E501
        'wrapped_array': [[(int,)]],  # noqa: E501
        'name_string': [str],  # noqa: E501
        'name_number': [float],  # noqa: E501
        'name_integer': [int],  # noqa: E501
        'name_boolean': [bool],  # noqa: E501
        'name_array': [[(int,)]],  # noqa: E501
        'name_wrapped_array': [[(int,)]],  # noqa: E501
        'prefix_string': [str],  # noqa: E501
        'prefix_number': [float],  # noqa: E501
        'prefix_integer': [int],  # noqa: E501
        'prefix_boolean': [bool],  # noqa: E501
        'prefix_array': [[(int,)]],  # noqa: E501
        'prefix_wrapped_array': [[(int,)]],  # noqa: E501
        'namespace_string': [str],  # noqa: E501
        'namespace_number': [float],  # noqa: E501
        'namespace_integer': [int],  # noqa: E501
        'namespace_boolean': [bool],  # noqa: E501
        'namespace_array': [[(int,)]],  # noqa: E501
        'namespace_wrapped_array': [[(int,)]],  # noqa: E501
        'prefix_ns_string': [str],  # noqa: E501
        'prefix_ns_number': [float],  # noqa: E501
        'prefix_ns_integer': [int],  # noqa: E501
        'prefix_ns_boolean': [bool],  # noqa: E501
        'prefix_ns_array': [[(int,)]],  # noqa: E501
        'prefix_ns_wrapped_array': [[(int,)]]  # noqa: E501
    }
    attribute_map = {
        'attribute_string': 'attribute_string',  # noqa: E501
        'attribute_number': 'attribute_number',  # noqa: E501
        'attribute_integer': 'attribute_integer',  # noqa: E501
        'attribute_boolean': 'attribute_boolean',  # noqa: E501
        'wrapped_array': 'wrapped_array',  # noqa: E501
        'name_string': 'name_string',  # noqa: E501
        'name_number': 'name_number',  # noqa: E501
        'name_integer': 'name_integer',  # noqa: E501
        'name_boolean': 'name_boolean',  # noqa: E501
        'name_array': 'name_array',  # noqa: E501
        'name_wrapped_array': 'name_wrapped_array',  # noqa: E501
        'prefix_string': 'prefix_string',  # noqa: E501
        'prefix_number': 'prefix_number',  # noqa: E501
        'prefix_integer': 'prefix_integer',  # noqa: E501
        'prefix_boolean': 'prefix_boolean',  # noqa: E501
        'prefix_array': 'prefix_array',  # noqa: E501
        'prefix_wrapped_array': 'prefix_wrapped_array',  # noqa: E501
        'namespace_string': 'namespace_string',  # noqa: E501
        'namespace_number': 'namespace_number',  # noqa: E501
        'namespace_integer': 'namespace_integer',  # noqa: E501
        'namespace_boolean': 'namespace_boolean',  # noqa: E501
        'namespace_array': 'namespace_array',  # noqa: E501
        'namespace_wrapped_array': 'namespace_wrapped_array',  # noqa: E501
        'prefix_ns_string': 'prefix_ns_string',  # noqa: E501
        'prefix_ns_number': 'prefix_ns_number',  # noqa: E501
        'prefix_ns_integer': 'prefix_ns_integer',  # noqa: E501
        'prefix_ns_boolean': 'prefix_ns_boolean',  # noqa: E501
        'prefix_ns_array': 'prefix_ns_array',  # noqa: E501
        'prefix_ns_wrapped_array': 'prefix_ns_wrapped_array'  # noqa: E501
    }

    def __init__(self, _check_type=False, **kwargs):  # noqa: E501
        """XmlItem - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            attribute_string (str): [optional] if omitted the server will use the default value of 'string'  # noqa: E501
            attribute_number (float): [optional] if omitted the server will use the default value of 1.234  # noqa: E501
            attribute_integer (int): [optional] if omitted the server will use the default value of -2  # noqa: E501
            attribute_boolean (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            wrapped_array ([(int,)]): [optional]  # noqa: E501
            name_string (str): [optional] if omitted the server will use the default value of 'string'  # noqa: E501
            name_number (float): [optional] if omitted the server will use the default value of 1.234  # noqa: E501
            name_integer (int): [optional] if omitted the server will use the default value of -2  # noqa: E501
            name_boolean (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            name_array ([(int,)]): [optional]  # noqa: E501
            name_wrapped_array ([(int,)]): [optional]  # noqa: E501
            prefix_string (str): [optional] if omitted the server will use the default value of 'string'  # noqa: E501
            prefix_number (float): [optional] if omitted the server will use the default value of 1.234  # noqa: E501
            prefix_integer (int): [optional] if omitted the server will use the default value of -2  # noqa: E501
            prefix_boolean (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            prefix_array ([(int,)]): [optional]  # noqa: E501
            prefix_wrapped_array ([(int,)]): [optional]  # noqa: E501
            namespace_string (str): [optional] if omitted the server will use the default value of 'string'  # noqa: E501
            namespace_number (float): [optional] if omitted the server will use the default value of 1.234  # noqa: E501
            namespace_integer (int): [optional] if omitted the server will use the default value of -2  # noqa: E501
            namespace_boolean (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            namespace_array ([(int,)]): [optional]  # noqa: E501
            namespace_wrapped_array ([(int,)]): [optional]  # noqa: E501
            prefix_ns_string (str): [optional] if omitted the server will use the default value of 'string'  # noqa: E501
            prefix_ns_number (float): [optional] if omitted the server will use the default value of 1.234  # noqa: E501
            prefix_ns_integer (int): [optional] if omitted the server will use the default value of -2  # noqa: E501
            prefix_ns_boolean (bool): [optional] if omitted the server will use the default value of True  # noqa: E501
            prefix_ns_array ([(int,)]): [optional]  # noqa: E501
            prefix_ns_wrapped_array ([(int,)]): [optional]  # noqa: E501
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
    def attribute_string(self):
        """Gets the attribute_string of this XmlItem.  # noqa: E501


        Returns:
            (str): The attribute_string of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('attribute_string')

    @attribute_string.setter
    def attribute_string(
            self, attribute_string):
        """Sets the attribute_string of this XmlItem.


        Returns:
            (str): The attribute_string of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'attribute_string',
            attribute_string
        )

    @property
    def attribute_number(self):
        """Gets the attribute_number of this XmlItem.  # noqa: E501


        Returns:
            (float): The attribute_number of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('attribute_number')

    @attribute_number.setter
    def attribute_number(
            self, attribute_number):
        """Sets the attribute_number of this XmlItem.


        Returns:
            (float): The attribute_number of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'attribute_number',
            attribute_number
        )

    @property
    def attribute_integer(self):
        """Gets the attribute_integer of this XmlItem.  # noqa: E501


        Returns:
            (int): The attribute_integer of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('attribute_integer')

    @attribute_integer.setter
    def attribute_integer(
            self, attribute_integer):
        """Sets the attribute_integer of this XmlItem.


        Returns:
            (int): The attribute_integer of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'attribute_integer',
            attribute_integer
        )

    @property
    def attribute_boolean(self):
        """Gets the attribute_boolean of this XmlItem.  # noqa: E501


        Returns:
            (bool): The attribute_boolean of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('attribute_boolean')

    @attribute_boolean.setter
    def attribute_boolean(
            self, attribute_boolean):
        """Sets the attribute_boolean of this XmlItem.


        Returns:
            (bool): The attribute_boolean of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'attribute_boolean',
            attribute_boolean
        )

    @property
    def wrapped_array(self):
        """Gets the wrapped_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The wrapped_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('wrapped_array')

    @wrapped_array.setter
    def wrapped_array(
            self, wrapped_array):
        """Sets the wrapped_array of this XmlItem.


        Returns:
            ([(int,)]): The wrapped_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'wrapped_array',
            wrapped_array
        )

    @property
    def name_string(self):
        """Gets the name_string of this XmlItem.  # noqa: E501


        Returns:
            (str): The name_string of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_string')

    @name_string.setter
    def name_string(
            self, name_string):
        """Sets the name_string of this XmlItem.


        Returns:
            (str): The name_string of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_string',
            name_string
        )

    @property
    def name_number(self):
        """Gets the name_number of this XmlItem.  # noqa: E501


        Returns:
            (float): The name_number of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_number')

    @name_number.setter
    def name_number(
            self, name_number):
        """Sets the name_number of this XmlItem.


        Returns:
            (float): The name_number of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_number',
            name_number
        )

    @property
    def name_integer(self):
        """Gets the name_integer of this XmlItem.  # noqa: E501


        Returns:
            (int): The name_integer of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_integer')

    @name_integer.setter
    def name_integer(
            self, name_integer):
        """Sets the name_integer of this XmlItem.


        Returns:
            (int): The name_integer of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_integer',
            name_integer
        )

    @property
    def name_boolean(self):
        """Gets the name_boolean of this XmlItem.  # noqa: E501


        Returns:
            (bool): The name_boolean of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_boolean')

    @name_boolean.setter
    def name_boolean(
            self, name_boolean):
        """Sets the name_boolean of this XmlItem.


        Returns:
            (bool): The name_boolean of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_boolean',
            name_boolean
        )

    @property
    def name_array(self):
        """Gets the name_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The name_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_array')

    @name_array.setter
    def name_array(
            self, name_array):
        """Sets the name_array of this XmlItem.


        Returns:
            ([(int,)]): The name_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_array',
            name_array
        )

    @property
    def name_wrapped_array(self):
        """Gets the name_wrapped_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The name_wrapped_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('name_wrapped_array')

    @name_wrapped_array.setter
    def name_wrapped_array(
            self, name_wrapped_array):
        """Sets the name_wrapped_array of this XmlItem.


        Returns:
            ([(int,)]): The name_wrapped_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'name_wrapped_array',
            name_wrapped_array
        )

    @property
    def prefix_string(self):
        """Gets the prefix_string of this XmlItem.  # noqa: E501


        Returns:
            (str): The prefix_string of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_string')

    @prefix_string.setter
    def prefix_string(
            self, prefix_string):
        """Sets the prefix_string of this XmlItem.


        Returns:
            (str): The prefix_string of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_string',
            prefix_string
        )

    @property
    def prefix_number(self):
        """Gets the prefix_number of this XmlItem.  # noqa: E501


        Returns:
            (float): The prefix_number of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_number')

    @prefix_number.setter
    def prefix_number(
            self, prefix_number):
        """Sets the prefix_number of this XmlItem.


        Returns:
            (float): The prefix_number of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_number',
            prefix_number
        )

    @property
    def prefix_integer(self):
        """Gets the prefix_integer of this XmlItem.  # noqa: E501


        Returns:
            (int): The prefix_integer of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_integer')

    @prefix_integer.setter
    def prefix_integer(
            self, prefix_integer):
        """Sets the prefix_integer of this XmlItem.


        Returns:
            (int): The prefix_integer of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_integer',
            prefix_integer
        )

    @property
    def prefix_boolean(self):
        """Gets the prefix_boolean of this XmlItem.  # noqa: E501


        Returns:
            (bool): The prefix_boolean of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_boolean')

    @prefix_boolean.setter
    def prefix_boolean(
            self, prefix_boolean):
        """Sets the prefix_boolean of this XmlItem.


        Returns:
            (bool): The prefix_boolean of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_boolean',
            prefix_boolean
        )

    @property
    def prefix_array(self):
        """Gets the prefix_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The prefix_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_array')

    @prefix_array.setter
    def prefix_array(
            self, prefix_array):
        """Sets the prefix_array of this XmlItem.


        Returns:
            ([(int,)]): The prefix_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_array',
            prefix_array
        )

    @property
    def prefix_wrapped_array(self):
        """Gets the prefix_wrapped_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The prefix_wrapped_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_wrapped_array')

    @prefix_wrapped_array.setter
    def prefix_wrapped_array(
            self, prefix_wrapped_array):
        """Sets the prefix_wrapped_array of this XmlItem.


        Returns:
            ([(int,)]): The prefix_wrapped_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_wrapped_array',
            prefix_wrapped_array
        )

    @property
    def namespace_string(self):
        """Gets the namespace_string of this XmlItem.  # noqa: E501


        Returns:
            (str): The namespace_string of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_string')

    @namespace_string.setter
    def namespace_string(
            self, namespace_string):
        """Sets the namespace_string of this XmlItem.


        Returns:
            (str): The namespace_string of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_string',
            namespace_string
        )

    @property
    def namespace_number(self):
        """Gets the namespace_number of this XmlItem.  # noqa: E501


        Returns:
            (float): The namespace_number of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_number')

    @namespace_number.setter
    def namespace_number(
            self, namespace_number):
        """Sets the namespace_number of this XmlItem.


        Returns:
            (float): The namespace_number of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_number',
            namespace_number
        )

    @property
    def namespace_integer(self):
        """Gets the namespace_integer of this XmlItem.  # noqa: E501


        Returns:
            (int): The namespace_integer of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_integer')

    @namespace_integer.setter
    def namespace_integer(
            self, namespace_integer):
        """Sets the namespace_integer of this XmlItem.


        Returns:
            (int): The namespace_integer of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_integer',
            namespace_integer
        )

    @property
    def namespace_boolean(self):
        """Gets the namespace_boolean of this XmlItem.  # noqa: E501


        Returns:
            (bool): The namespace_boolean of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_boolean')

    @namespace_boolean.setter
    def namespace_boolean(
            self, namespace_boolean):
        """Sets the namespace_boolean of this XmlItem.


        Returns:
            (bool): The namespace_boolean of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_boolean',
            namespace_boolean
        )

    @property
    def namespace_array(self):
        """Gets the namespace_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The namespace_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_array')

    @namespace_array.setter
    def namespace_array(
            self, namespace_array):
        """Sets the namespace_array of this XmlItem.


        Returns:
            ([(int,)]): The namespace_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_array',
            namespace_array
        )

    @property
    def namespace_wrapped_array(self):
        """Gets the namespace_wrapped_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The namespace_wrapped_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('namespace_wrapped_array')

    @namespace_wrapped_array.setter
    def namespace_wrapped_array(
            self, namespace_wrapped_array):
        """Sets the namespace_wrapped_array of this XmlItem.


        Returns:
            ([(int,)]): The namespace_wrapped_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'namespace_wrapped_array',
            namespace_wrapped_array
        )

    @property
    def prefix_ns_string(self):
        """Gets the prefix_ns_string of this XmlItem.  # noqa: E501


        Returns:
            (str): The prefix_ns_string of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_string')

    @prefix_ns_string.setter
    def prefix_ns_string(
            self, prefix_ns_string):
        """Sets the prefix_ns_string of this XmlItem.


        Returns:
            (str): The prefix_ns_string of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_string',
            prefix_ns_string
        )

    @property
    def prefix_ns_number(self):
        """Gets the prefix_ns_number of this XmlItem.  # noqa: E501


        Returns:
            (float): The prefix_ns_number of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_number')

    @prefix_ns_number.setter
    def prefix_ns_number(
            self, prefix_ns_number):
        """Sets the prefix_ns_number of this XmlItem.


        Returns:
            (float): The prefix_ns_number of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_number',
            prefix_ns_number
        )

    @property
    def prefix_ns_integer(self):
        """Gets the prefix_ns_integer of this XmlItem.  # noqa: E501


        Returns:
            (int): The prefix_ns_integer of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_integer')

    @prefix_ns_integer.setter
    def prefix_ns_integer(
            self, prefix_ns_integer):
        """Sets the prefix_ns_integer of this XmlItem.


        Returns:
            (int): The prefix_ns_integer of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_integer',
            prefix_ns_integer
        )

    @property
    def prefix_ns_boolean(self):
        """Gets the prefix_ns_boolean of this XmlItem.  # noqa: E501


        Returns:
            (bool): The prefix_ns_boolean of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_boolean')

    @prefix_ns_boolean.setter
    def prefix_ns_boolean(
            self, prefix_ns_boolean):
        """Sets the prefix_ns_boolean of this XmlItem.


        Returns:
            (bool): The prefix_ns_boolean of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_boolean',
            prefix_ns_boolean
        )

    @property
    def prefix_ns_array(self):
        """Gets the prefix_ns_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The prefix_ns_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_array')

    @prefix_ns_array.setter
    def prefix_ns_array(
            self, prefix_ns_array):
        """Sets the prefix_ns_array of this XmlItem.


        Returns:
            ([(int,)]): The prefix_ns_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_array',
            prefix_ns_array
        )

    @property
    def prefix_ns_wrapped_array(self):
        """Gets the prefix_ns_wrapped_array of this XmlItem.  # noqa: E501


        Returns:
            ([(int,)]): The prefix_ns_wrapped_array of this XmlItem.  # noqa: E501
        """
        return self._data_store.get('prefix_ns_wrapped_array')

    @prefix_ns_wrapped_array.setter
    def prefix_ns_wrapped_array(
            self, prefix_ns_wrapped_array):
        """Sets the prefix_ns_wrapped_array of this XmlItem.


        Returns:
            ([(int,)]): The prefix_ns_wrapped_array of this XmlItem.  # noqa: E501
        """

        self.__setitem__(
            'prefix_ns_wrapped_array',
            prefix_ns_wrapped_array
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
        if not isinstance(other, XmlItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
