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

from petstore_api.utils import recursive_type, valid_type


class Pet(object):
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
                            Optional and required variables only.
    """
    openapi_types = {
        'id': 'int',
        'category': 'Category',
        'name': 'str',
        'photo_urls': 'list[str]',
        'tags': 'list[Tag]',
        'status': 'str'
    }
    attribute_map = {
        'id': 'id',
        'category': 'category',
        'name': 'name',
        'photo_urls': 'photoUrls',
        'tags': 'tags',
        'status': 'status'
    }

    def __init__(self, photo_urls, name='doggie', _check_type=False, **kwargs):  # noqa: E501
        """Pet - a model defined in OpenAPI

        Args:
            photo_urls (list[str]):
            name (str): defaults to 'doggie', must be one of ['doggie']

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            id (int): [optional]
            category (Category): [optional]
            tags (list[Tag]): [optional]
            status (str): pet status in the store. [optional]
        """

        self._data_store = {}
        self.discriminator = None
        self._check_type = _check_type

        # assign using .var_name to check against nullable and enums
        self.name = name
        self.photo_urls = photo_urls
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
            raise KeyError("{0} has no key '{1}'".format(
                type(self).__name__, name))

        passed_type = recursive_type(value)
        if type(name) != str:
            raise TypeError('Variable name must be type string and %s was not' % name)
        elif check_type and not valid_type(passed_type, required_type):
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
    def id(self):
        """Gets the id of this Pet.  # noqa: E501


        :return: The id of this Pet.  # noqa: E501
        :rtype: int
        """
        return self._data_store.get('id')

    @id.setter
    def id(self, id):
        """Sets the id of this Pet.


        :param id: The id of this Pet.  # noqa: E501
        :type: int
        """

        self.__setitem__('id', id)

    @property
    def category(self):
        """Gets the category of this Pet.  # noqa: E501


        :return: The category of this Pet.  # noqa: E501
        :rtype: Category
        """
        return self._data_store.get('category')

    @category.setter
    def category(self, category):
        """Sets the category of this Pet.


        :param category: The category of this Pet.  # noqa: E501
        :type: Category
        """

        self.__setitem__('category', category)

    @property
    def name(self):
        """Gets the name of this Pet.  # noqa: E501


        :return: The name of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('name')

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.


        :param name: The name of this Pet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self.__setitem__('name', name)

    @property
    def photo_urls(self):
        """Gets the photo_urls of this Pet.  # noqa: E501


        :return: The photo_urls of this Pet.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_store.get('photo_urls')

    @photo_urls.setter
    def photo_urls(self, photo_urls):
        """Sets the photo_urls of this Pet.


        :param photo_urls: The photo_urls of this Pet.  # noqa: E501
        :type: list[str]
        """
        if photo_urls is None:
            raise ValueError("Invalid value for `photo_urls`, must not be `None`")  # noqa: E501

        self.__setitem__('photo_urls', photo_urls)

    @property
    def tags(self):
        """Gets the tags of this Pet.  # noqa: E501


        :return: The tags of this Pet.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._data_store.get('tags')

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Pet.


        :param tags: The tags of this Pet.  # noqa: E501
        :type: list[Tag]
        """

        self.__setitem__('tags', tags)

    @property
    def status(self):
        """Gets the status of this Pet.  # noqa: E501

        pet status in the store  # noqa: E501

        :return: The status of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._data_store.get('status')

    @status.setter
    def status(self, status):
        """Sets the status of this Pet.

        pet status in the store  # noqa: E501

        :param status: The status of this Pet.  # noqa: E501
        :type: str
        """
        allowed_values = ["available", "pending", "sold"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self.__setitem__('status', status)

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
        if not isinstance(other, Pet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
