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


class FormatTest(OpenApiModel):
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
        'integer': [int],  # noqa: E501
        'int32': [int],  # noqa: E501
        'int64': [int],  # noqa: E501
        'number': [float],  # noqa: E501
        'float': [float],  # noqa: E501
        'double': [float],  # noqa: E501
        'string': [str],  # noqa: E501
        'byte': [str],  # noqa: E501
        'binary': [file_type],  # noqa: E501
        'date': [date],  # noqa: E501
        'date_time': [datetime],  # noqa: E501
        'uuid': [str],  # noqa: E501
        'password': [str]  # noqa: E501
    }
    attribute_map = {
        'integer': 'integer',  # noqa: E501
        'int32': 'int32',  # noqa: E501
        'int64': 'int64',  # noqa: E501
        'number': 'number',  # noqa: E501
        'float': 'float',  # noqa: E501
        'double': 'double',  # noqa: E501
        'string': 'string',  # noqa: E501
        'byte': 'byte',  # noqa: E501
        'binary': 'binary',  # noqa: E501
        'date': 'date',  # noqa: E501
        'date_time': 'dateTime',  # noqa: E501
        'uuid': 'uuid',  # noqa: E501
        'password': 'password'  # noqa: E501
    }

    def __init__(self, number, byte, date, password, _check_type=False, **kwargs):  # noqa: E501
        """FormatTest - a model defined in OpenAPI

        Args:
            number (float):
            byte (str):
            date (date):
            password (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            integer (int): [optional]  # noqa: E501
            int32 (int): [optional]  # noqa: E501
            int64 (int): [optional]  # noqa: E501
            float (float): [optional]  # noqa: E501
            double (float): [optional]  # noqa: E501
            string (str): [optional]  # noqa: E501
            binary (file_type): [optional]  # noqa: E501
            date_time (datetime): [optional]  # noqa: E501
            uuid (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type

        # assign using .var_name to check against nullable and enums
        self.number = number
        self.byte = byte
        self.date = date
        self.password = password
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
    def integer(self):
        """Gets the integer of this FormatTest.  # noqa: E501


        Returns:
            (int): The integer of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('integer')

    @integer.setter
    def integer(
            self, integer):
        """Sets the integer of this FormatTest.


        Returns:
            (int): The integer of this FormatTest.  # noqa: E501
        """
        if integer is not None and integer > 100:  # noqa: E501
            raise ApiValueError("Invalid value for `integer`, must be a value less than or equal to `100`")  # noqa: E501
        if integer is not None and integer < 10:  # noqa: E501
            raise ApiValueError("Invalid value for `integer`, must be a value greater than or equal to `10`")  # noqa: E501

        self.__setitem__(
            'integer',
            integer
        )

    @property
    def int32(self):
        """Gets the int32 of this FormatTest.  # noqa: E501


        Returns:
            (int): The int32 of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('int32')

    @int32.setter
    def int32(
            self, int32):
        """Sets the int32 of this FormatTest.


        Returns:
            (int): The int32 of this FormatTest.  # noqa: E501
        """
        if int32 is not None and int32 > 200:  # noqa: E501
            raise ApiValueError("Invalid value for `int32`, must be a value less than or equal to `200`")  # noqa: E501
        if int32 is not None and int32 < 20:  # noqa: E501
            raise ApiValueError("Invalid value for `int32`, must be a value greater than or equal to `20`")  # noqa: E501

        self.__setitem__(
            'int32',
            int32
        )

    @property
    def int64(self):
        """Gets the int64 of this FormatTest.  # noqa: E501


        Returns:
            (int): The int64 of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('int64')

    @int64.setter
    def int64(
            self, int64):
        """Sets the int64 of this FormatTest.


        Returns:
            (int): The int64 of this FormatTest.  # noqa: E501
        """

        self.__setitem__(
            'int64',
            int64
        )

    @property
    def number(self):
        """Gets the number of this FormatTest.  # noqa: E501


        Returns:
            (float): The number of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('number')

    @number.setter
    def number(
            self, number):
        """Sets the number of this FormatTest.


        Returns:
            (float): The number of this FormatTest.  # noqa: E501
        """
        if number is None:
            raise ApiValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number is not None and number > 543.2:  # noqa: E501
            raise ApiValueError("Invalid value for `number`, must be a value less than or equal to `543.2`")  # noqa: E501
        if number is not None and number < 32.1:  # noqa: E501
            raise ApiValueError("Invalid value for `number`, must be a value greater than or equal to `32.1`")  # noqa: E501

        self.__setitem__(
            'number',
            number
        )

    @property
    def float(self):
        """Gets the float of this FormatTest.  # noqa: E501


        Returns:
            (float): The float of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('float')

    @float.setter
    def float(
            self, float):
        """Sets the float of this FormatTest.


        Returns:
            (float): The float of this FormatTest.  # noqa: E501
        """
        if float is not None and float > 987.6:  # noqa: E501
            raise ApiValueError("Invalid value for `float`, must be a value less than or equal to `987.6`")  # noqa: E501
        if float is not None and float < 54.3:  # noqa: E501
            raise ApiValueError("Invalid value for `float`, must be a value greater than or equal to `54.3`")  # noqa: E501

        self.__setitem__(
            'float',
            float
        )

    @property
    def double(self):
        """Gets the double of this FormatTest.  # noqa: E501


        Returns:
            (float): The double of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('double')

    @double.setter
    def double(
            self, double):
        """Sets the double of this FormatTest.


        Returns:
            (float): The double of this FormatTest.  # noqa: E501
        """
        if double is not None and double > 123.4:  # noqa: E501
            raise ApiValueError("Invalid value for `double`, must be a value less than or equal to `123.4`")  # noqa: E501
        if double is not None and double < 67.8:  # noqa: E501
            raise ApiValueError("Invalid value for `double`, must be a value greater than or equal to `67.8`")  # noqa: E501

        self.__setitem__(
            'double',
            double
        )

    @property
    def string(self):
        """Gets the string of this FormatTest.  # noqa: E501


        Returns:
            (str): The string of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('string')

    @string.setter
    def string(
            self, string):
        """Sets the string of this FormatTest.


        Returns:
            (str): The string of this FormatTest.  # noqa: E501
        """
        if string is not None and not re.search(r'', string):  # noqa: E501
            raise ApiValueError(r"Invalid value for `string`, must be a follow pattern or equal to `/[a-z]/i`")  # noqa: E501

        self.__setitem__(
            'string',
            string
        )

    @property
    def byte(self):
        """Gets the byte of this FormatTest.  # noqa: E501


        Returns:
            (str): The byte of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('byte')

    @byte.setter
    def byte(
            self, byte):
        """Sets the byte of this FormatTest.


        Returns:
            (str): The byte of this FormatTest.  # noqa: E501
        """
        if byte is None:
            raise ApiValueError("Invalid value for `byte`, must not be `None`")  # noqa: E501
        if byte is not None and not re.search(r'', byte):  # noqa: E501
            raise ApiValueError(r"Invalid value for `byte`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self.__setitem__(
            'byte',
            byte
        )

    @property
    def binary(self):
        """Gets the binary of this FormatTest.  # noqa: E501


        Returns:
            (file_type): The binary of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('binary')

    @binary.setter
    def binary(
            self, binary):
        """Sets the binary of this FormatTest.


        Returns:
            (file_type): The binary of this FormatTest.  # noqa: E501
        """

        self.__setitem__(
            'binary',
            binary
        )

    @property
    def date(self):
        """Gets the date of this FormatTest.  # noqa: E501


        Returns:
            (date): The date of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('date')

    @date.setter
    def date(
            self, date):
        """Sets the date of this FormatTest.


        Returns:
            (date): The date of this FormatTest.  # noqa: E501
        """
        if date is None:
            raise ApiValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'date',
            date
        )

    @property
    def date_time(self):
        """Gets the date_time of this FormatTest.  # noqa: E501


        Returns:
            (datetime): The date_time of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('date_time')

    @date_time.setter
    def date_time(
            self, date_time):
        """Sets the date_time of this FormatTest.


        Returns:
            (datetime): The date_time of this FormatTest.  # noqa: E501
        """

        self.__setitem__(
            'date_time',
            date_time
        )

    @property
    def uuid(self):
        """Gets the uuid of this FormatTest.  # noqa: E501


        Returns:
            (str): The uuid of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('uuid')

    @uuid.setter
    def uuid(
            self, uuid):
        """Sets the uuid of this FormatTest.


        Returns:
            (str): The uuid of this FormatTest.  # noqa: E501
        """

        self.__setitem__(
            'uuid',
            uuid
        )

    @property
    def password(self):
        """Gets the password of this FormatTest.  # noqa: E501


        Returns:
            (str): The password of this FormatTest.  # noqa: E501
        """
        return self._data_store.get('password')

    @password.setter
    def password(
            self, password):
        """Sets the password of this FormatTest.


        Returns:
            (str): The password of this FormatTest.  # noqa: E501
        """
        if password is None:
            raise ApiValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 64:
            raise ApiValueError("Invalid value for `password`, length must be less than or equal to `64`")  # noqa: E501
        if password is not None and len(password) < 10:
            raise ApiValueError("Invalid value for `password`, length must be greater than or equal to `10`")  # noqa: E501

        self.__setitem__(
            'password',
            password
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
        if not isinstance(other, FormatTest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
