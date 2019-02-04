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


class HasOnlyReadOnly(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'bar': 'str',
        'foo': 'str'
    }
    attribute_map = {
        'bar': 'bar',
        'foo': 'foo'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """HasOnlyReadOnly - a model defined in OpenAPI



        Keyword Args:
            bar (str): [optional]
            foo (str): [optional]

        """  # noqa: E501

        self._data_store = {}

        self.discriminator = None

        for var_name, var_value in six.iteritems(kwargs):
            self.__setitem__(var_name, var_value)

    def recursive_type(self, item):
        """Gets a string describing the full the recursive type of a value"""
        item_type = type(item)
        if item_type == dict:
            child_key_types = set()
            child_value_types = set()
            for child_key, child_value in six.iteritems(item):
                child_key_types.add(self.recursive_type(child_key))
                child_value_types.add(self.recursive_type(child_value))
            if child_key_types != set(['str']):
                raise ValueError('Invalid dict key type. All Openapi dict keys must be strings')
            child_value_types = '|'.join(sorted(list(child_value_types)))
            return "dict(str, {0})".format(child_value_types)
        elif item_type == list:
            child_value_types = set()
            for child_item in item:
                child_value_types.add(self.recursive_type(child_item))
            child_value_types = '|'.join(sorted(list(child_value_types)))
            return "list[{0}]".format(child_value_types)
        else:
            return type(item).__name__

    def __setitem__(self, name, value):
        check_type = False
        if name in self.openapi_types:
            required_type = self.openapi_types[name]
        else:
            raise KeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        passed_type = self.recursive_type(value)
        if type(name) != str:
            raise TypeError('Variable name must be type string and %s was not' % name)
        elif passed_type != required_type and check_type:
            raise ValueError('Variable value must be type %s but you passed in %s' %
                             (required_type, passed_type))

        if name in self.openapi_types:
            setattr(self, name, value)
        else:
            self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]
        raise KeyError("{0} has no key {1}".format(
            type(self).__name__, name))

    @property
    def bar(self):
        """Gets the bar of this HasOnlyReadOnly.  # noqa: E501


        :return: The bar of this HasOnlyReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('bar')

    @bar.setter
    def bar(self, bar):
        """Sets the bar of this HasOnlyReadOnly.


        :param bar: The bar of this HasOnlyReadOnly.  # noqa: E501
        :type: str
        """

        self._data_store['bar'] = bar

    @property
    def foo(self):
        """Gets the foo of this HasOnlyReadOnly.  # noqa: E501


        :return: The foo of this HasOnlyReadOnly.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('foo')

    @foo.setter
    def foo(self, foo):
        """Sets the foo of this HasOnlyReadOnly.


        :param foo: The foo of this HasOnlyReadOnly.  # noqa: E501
        :type: str
        """

        self._data_store['foo'] = foo

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, value in six.iteritems(self._data_store):
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HasOnlyReadOnly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
