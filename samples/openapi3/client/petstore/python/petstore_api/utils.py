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

def recursive_type(item):
    """Gets a string describing the full the recursive type of a value"""
    item_type = type(item)
    if item_type == dict:
        child_key_types = set()
        child_value_types = set()
        for child_key, child_value in six.iteritems(item):
            child_key_types.add(recursive_type(child_key))
            child_value_types.add(recursive_type(child_value))
        # only allow empty dicts or dicts with str keys
        if child_key_types not in [set(['str']), set()]:
            raise TypeError('Invalid dict key type. All Openapi dict keys must be strings')
        child_value_types = TYPE_SEPARATOR.join(sorted(list(child_value_types)))
        if child_key_types == set():
            return "dict()"
        return "dict(str, {0})".format(child_value_types)
    elif item_type == list:
        child_value_types = set()
        for child_item in item:
            child_value_types.add(recursive_type(child_item))
        child_value_types = TYPE_SEPARATOR.join(sorted(list(child_value_types)))
        return "list[{0}]".format(child_value_types)
    else:
        return type(item).__name__


class OpenaApiTypeError(TypeError):
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
        super(OpenaApiTypeError, self).__init__(msg)
        self.path_to_item = path_to_item
        self.current_item = current_item
        self.required_types = required_types


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
    if not isinstance(input_value, required_type_classes):
        raise OpenaApiTypeError(
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
                raise OpenaApiTypeError(
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
