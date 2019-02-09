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


class Capitalization(object):
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
        'small_camel': 'str',
        'capital_camel': 'str',
        'small_snake': 'str',
        'capital_snake': 'str',
        'sca_eth_flow_points': 'str',
        'att_name': 'str'
    }
    attribute_map = {
        'small_camel': 'smallCamel',
        'capital_camel': 'CapitalCamel',
        'small_snake': 'small_Snake',
        'capital_snake': 'Capital_Snake',
        'sca_eth_flow_points': 'SCA_ETH_Flow_Points',
        'att_name': 'ATT_NAME'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """Capitalization - a model defined in OpenAPI



        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wront type is input.
                                Defaults to False
            small_camel (str): [optional]
            capital_camel (str): [optional]
            small_snake (str): [optional]
            capital_snake (str): [optional]
            sca_eth_flow_points (str): [optional]
            att_name (str): Name of the pet . [optional]
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

    @property
    def small_camel(self):
        """Gets the small_camel of this Capitalization.  # noqa: E501


        :return: The small_camel of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('small_camel')

    @small_camel.setter
    def small_camel(self, small_camel):
        """Sets the small_camel of this Capitalization.


        :param small_camel: The small_camel of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('small_camel', small_camel)

    @property
    def capital_camel(self):
        """Gets the capital_camel of this Capitalization.  # noqa: E501


        :return: The capital_camel of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('capital_camel')

    @capital_camel.setter
    def capital_camel(self, capital_camel):
        """Sets the capital_camel of this Capitalization.


        :param capital_camel: The capital_camel of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('capital_camel', capital_camel)

    @property
    def small_snake(self):
        """Gets the small_snake of this Capitalization.  # noqa: E501


        :return: The small_snake of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('small_snake')

    @small_snake.setter
    def small_snake(self, small_snake):
        """Sets the small_snake of this Capitalization.


        :param small_snake: The small_snake of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('small_snake', small_snake)

    @property
    def capital_snake(self):
        """Gets the capital_snake of this Capitalization.  # noqa: E501


        :return: The capital_snake of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('capital_snake')

    @capital_snake.setter
    def capital_snake(self, capital_snake):
        """Sets the capital_snake of this Capitalization.


        :param capital_snake: The capital_snake of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('capital_snake', capital_snake)

    @property
    def sca_eth_flow_points(self):
        """Gets the sca_eth_flow_points of this Capitalization.  # noqa: E501


        :return: The sca_eth_flow_points of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('sca_eth_flow_points')

    @sca_eth_flow_points.setter
    def sca_eth_flow_points(self, sca_eth_flow_points):
        """Sets the sca_eth_flow_points of this Capitalization.


        :param sca_eth_flow_points: The sca_eth_flow_points of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('sca_eth_flow_points', sca_eth_flow_points)

    @property
    def att_name(self):
        """Gets the att_name of this Capitalization.  # noqa: E501

        Name of the pet   # noqa: E501

        :return: The att_name of this Capitalization.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('att_name')

    @att_name.setter
    def att_name(self, att_name):
        """Sets the att_name of this Capitalization.

        Name of the pet   # noqa: E501

        :param att_name: The att_name of this Capitalization.  # noqa: E501
        :type: str
        """

        self.__setitem__('att_name', att_name)

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
        if not isinstance(other, Capitalization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
