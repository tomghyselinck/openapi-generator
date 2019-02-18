# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from datetime import date, datetime
import re

import six

none_type = type(None)
if six.PY3:
    import io
    file_type = io.IOBase
else:
    file_type = file


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, required_types, current_item, path_to_item,
                 value_type=True):
        key_or_value = 'value'
        if not value_type:
            key_or_value = 'key'
        msg = ("Invalid type for variable {0}. Required {1} type is {2} and "
               "passed type was {3} at location={4}".format(
               path_to_item[0],
               key_or_value,
               required_types,
               type(current_item),
               path_to_item
               ))
        super(ApiTypeError, self).__init__(msg)
        self.path_to_item = path_to_item
        self.current_item = current_item
        self.required_types = required_types


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg):
        super(ApiTypeError, self).__init__(msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg):
        super(ApiKeyError, self).__init__(msg)


def get_required_type_classes(required_types):
    """Converts the tuple required_types into a tuple of its child classes

    required_type will contain either classes or instance of list or dict
    so convert it to a tuple of classes
    """
    results = []
    child_required_types = {}
    for required_type in required_types:
        if isinstance(required_type, list):
            results.append(list)
            child_required_types[list] = required_type[0]
        elif isinstance(required_type, dict):
            results.append(dict)
            child_required_types[dict] = required_type[str]
        else:
            results.append(required_type)
    return tuple(results), child_required_types


def validate_type(input_value, required_types, variable_path):
    """Raises a TypeError is ther is a problem, otherwise continue"""
    results = get_required_type_classes(required_types)
    required_type_classes, child_required_types = results
    # Note: we can't use isinstance here because isinstance(True, int) == True
    if not type(input_value) in required_type_classes:
        raise ApiTypeError(
            required_type_classes,
            input_value,
            variable_path
        )
    # input_value's type is in required_type_classes
    if child_required_types == {}:
        # all types are of the required types and there are no more inner
        # variables left to look at
        return
    inner_required_types = child_required_types.get(type(input_value))
    if inner_required_types is None:
        # for this type, there are not more inner variables left to look at
        return
    if isinstance(input_value, list):
        if input_value == []:
            # allow an empty list
            return
        for index, inner_value in enumerate(input_value):
            inner_path = list(variable_path)
            inner_path.append(index)
            validate_type(inner_value, inner_required_types, inner_path)
    elif isinstance(input_value, dict):
        if input_value == {}:
            # allow an empty dict
            return
        for inner_key, inner_val in six.iteritems(input_value):
            inner_path = list(variable_path)
            inner_path.append(inner_key)
            if not isinstance(inner_key, str):
                raise ApiTypeError(
                    (str,),
                    inner_key,
                    inner_path,
                    value_type=False
                )
            validate_type(inner_val, inner_required_types, inner_path)


def model_to_dict(model_instance, serialize=True):
    """Returns the model properties as a dict

    Args:
        model_instance (one of your model instances): the model instance that
            will be converted to a dict.

    Keyword Args:
        serialize (bool): if True, the keys in the dict will be values from
            attribute_map
    """
    result = {}

    for attr, value in six.iteritems(model_instance._data_store):
        if serialize:
            attr = model_instance.attribute_map[attr]
        if isinstance(value, list):
            result[attr] = list(map(
                lambda x: model_to_dict(x, serialize=serialize)
                if hasattr(x, '_data_store') else x, value
            ))
        elif isinstance(value, dict):
            result[attr] = dict(map(
                lambda item: (item[0], model_to_dict(item[1], serialize=serialize))
                if hasattr(item[1], '_data_store') else item,
                value.items()
            ))
        elif hasattr(value, '_data_store'):
            result[attr] = model_to_dict(value, serialize=serialize)
        else:
            result[attr] = value

    return result
