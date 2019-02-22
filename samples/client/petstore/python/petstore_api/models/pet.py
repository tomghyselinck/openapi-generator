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
from petstore_api.models.category import Category
from petstore_api.models.tag import Tag


class Pet(OpenApiModel):
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
        'id': [int],  # noqa: E501
        'category': [Category],  # noqa: E501
        'name': [str],  # noqa: E501
        'photo_urls': [[(str,)]],  # noqa: E501
        'tags': [[(Tag,)]],  # noqa: E501
        'status': [str]  # noqa: E501
    }
    attribute_map = {
        'id': 'id',  # noqa: E501
        'category': 'category',  # noqa: E501
        'name': 'name',  # noqa: E501
        'photo_urls': 'photoUrls',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'status': 'status'  # noqa: E501
    }

    def __init__(self, photo_urls, name='doggie', _check_type=False, **kwargs):  # noqa: E501
        """Pet - a model defined in OpenAPI

        Args:
            photo_urls ([(str,)]):
            name (str): defaults to 'doggie', must be one of ['doggie']  # noqa: E501

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to False
            id (int): [optional]  # noqa: E501
            category (Category): [optional]  # noqa: E501
            tags ([(Tag,)]): [optional]  # noqa: E501
            status (str): pet status in the store. [optional]  # noqa: E501
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
        """Gets the id of this Pet.  # noqa: E501


        Returns:
            (int): The id of this Pet.  # noqa: E501
        """
        return self._data_store.get('id')

    @id.setter
    def id(
            self, id):
        """Sets the id of this Pet.


        Returns:
            (int): The id of this Pet.  # noqa: E501
        """

        self.__setitem__(
            'id',
            id
        )

    @property
    def category(self):
        """Gets the category of this Pet.  # noqa: E501


        Returns:
            (Category): The category of this Pet.  # noqa: E501
        """
        return self._data_store.get('category')

    @category.setter
    def category(
            self, category):
        """Sets the category of this Pet.


        Returns:
            (Category): The category of this Pet.  # noqa: E501
        """

        self.__setitem__(
            'category',
            category
        )

    @property
    def name(self):
        """Gets the name of this Pet.  # noqa: E501


        Returns:
            (str): The name of this Pet.  # noqa: E501
        """
        return self._data_store.get('name')

    @name.setter
    def name(
            self, name):
        """Sets the name of this Pet.


        Returns:
            (str): The name of this Pet.  # noqa: E501
        """
        if name is None:
            raise ApiValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'name',
            name
        )

    @property
    def photo_urls(self):
        """Gets the photo_urls of this Pet.  # noqa: E501


        Returns:
            ([(str,)]): The photo_urls of this Pet.  # noqa: E501
        """
        return self._data_store.get('photo_urls')

    @photo_urls.setter
    def photo_urls(
            self, photo_urls):
        """Sets the photo_urls of this Pet.


        Returns:
            ([(str,)]): The photo_urls of this Pet.  # noqa: E501
        """
        if photo_urls is None:
            raise ApiValueError("Invalid value for `photo_urls`, must not be `None`")  # noqa: E501

        self.__setitem__(
            'photo_urls',
            photo_urls
        )

    @property
    def tags(self):
        """Gets the tags of this Pet.  # noqa: E501


        Returns:
            ([(Tag,)]): The tags of this Pet.  # noqa: E501
        """
        return self._data_store.get('tags')

    @tags.setter
    def tags(
            self, tags):
        """Sets the tags of this Pet.


        Returns:
            ([(Tag,)]): The tags of this Pet.  # noqa: E501
        """

        self.__setitem__(
            'tags',
            tags
        )

    @property
    def status(self):
        """Gets the status of this Pet.  # noqa: E501

        pet status in the store  # noqa: E501

        Returns:
            (str): The status of this Pet.  # noqa: E501
        """
        return self._data_store.get('status')

    @status.setter
    def status(
            self, status):
        """Sets the status of this Pet.

        pet status in the store  # noqa: E501

        Returns:
            (str): The status of this Pet.  # noqa: E501
        """
        allowed_values = ["available", "pending", "sold"]  # noqa: E501
        if status not in allowed_values:
            raise ApiValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self.__setitem__(
            'status',
            status
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
        if not isinstance(other, Pet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
