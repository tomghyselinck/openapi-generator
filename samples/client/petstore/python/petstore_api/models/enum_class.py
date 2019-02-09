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


class EnumClass(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _ABC = "_abc"
    _EFG = "-efg"
    _XYZ_ = "(xyz)"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }
    attribute_map = {
    }

    def __init__(self, **kwargs):  # noqa: E501
        """EnumClass - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wront type is input.
                                Defaults to False
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = kwargs.get('_check_type') or False

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
            # only allow empty dicts or dicts with str keys
            if child_key_types not in [set(['str']), set()]:
                raise TypeError('Invalid dict key type. All Openapi dict keys must be strings')
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

    def valid_type(self, passed_type_str, required_type_str):
        """Returns a boolean, True if passed_type is required_type"""
        if passed_type_str == required_type_str:
            return True
        req_types, req_remainder = self.get_types_remainder(required_type_str)
        passed_types, passed_remainder = self.get_types_remainder(passed_type_str)
        if not passed_types.issubset(req_types):
            return False
        # passed_types is in req_types
        if req_remainder == '':
            return True
        if (passed_types == set(['list']) and passed_remainder == '' and
                all(char not in req_remainder for char in '([')):
            # we have an empty list, and the inner required types are
            # primitives like str, int etc, allow it
            return True
        return self.valid_type(passed_remainder, req_remainder)

    def get_types_remainder(self, type_string):
        container_types = [('dict(str, ', ')'), ('list[', ']')]
        for type_prefix, type_suffix in container_types:
            if type_string.startswith(type_prefix) and type_string.endswith(type_suffix):
                return set([type_prefix[:4]]), type_string[len(type_prefix):-1]
        type_set = set(type_string.split('|'))
        return type_set, ''

    def __setitem__(self, name, value):
        if name in self.openapi_types:
            check_type = self._check_type
            required_type = self.openapi_types[name]
        else:
            raise KeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        passed_type = self.recursive_type(value)
        if type(name) != str:
            raise TypeError('Variable name must be type string and %s was not' % name)
        elif check_type and not self.valid_type(passed_type, required_type):
            raise TypeError('Variable value must be type %s but you passed in %s' %
                            (required_type, passed_type))

        self._data_store[name] = value

    def __getitem__(self, name):
        if name in self.openapi_types:
            return self._data_store.get(name)
        if name in self._data_store:
            return self._data_store[name]
        raise KeyError("{0} has no key {1}".format(
            type(self).__name__, name))

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
        if not isinstance(other, EnumClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
