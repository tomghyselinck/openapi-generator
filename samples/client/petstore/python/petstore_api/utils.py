# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from datetime import date, datetime  # noqa: F401

import six

none_type = type(None)
if six.PY3:
    import io
    file_type = io.IOBase
else:
    file_type = file  # noqa: F821


class OpenApiModel(object):
    """The base class for all OpenAPIModels"""

COERCION_INDEX_BY_TYPE = {
    none_type: 0,
    list: 1,
    OpenApiModel: 2,
    dict: 3,
    float: 4,
    int: 5,
    bool: 6,
    datetime: 7,
    date: 8,
    str: 9
}
COERCIBLE_TYPE_PAIRS = (
    (dict, OpenApiModel),
    (list, OpenApiModel),
    (str, int),
    (str, float),
    (str, datetime),
    (str, date),
    (int, str),
    (float, str),
    (str, file_type)
)


def order_response_types(required_types):
    """Returns the required types sorted in coercion order

    Args:
        required_types (list/tuple): collection of classes or instance of
            list or dict with classs information inside it

    Returns:
        (list/tuple): coercion order sorted collection of classes or instance
            of list or dict with classs information inside it
    """

    def index_getter(class_or_instance):
        if isinstance(class_or_instance, list):
            return COERCION_INDEX_BY_TYPE[list]
        elif isinstance(class_or_instance, dict):
            return COERCION_INDEX_BY_TYPE[dict]
        elif issubclass(class_or_instance, OpenApiModel):
            return COERCION_INDEX_BY_TYPE[OpenApiModel]
        return COERCION_INDEX_BY_TYPE[class_or_instance]

    sorted_types = sorted(
        required_types,
        key=lambda class_or_instance: index_getter(class_or_instance)
    )
    return sorted_types


def remove_uncoercible(required_types_classes, current_item):
    """Only keeps the type conversions that are possible

    Args:
        required_types_classes (tuple): tuple of classes that are required
        current_item (any): the current item to be converted

    Returns:
        (list): the remaining coercible required types, classes only
    """
    if isinstance(current_item, file_type):
        current_type = file_type
    else:
        current_type = type(current_item)

    results_classes = []
    for real_required_type_class in required_types_classes:
        required_type_class = real_required_type_class
        if issubclass(real_required_type_class, OpenApiModel):
            required_type_class = OpenApiModel
        class_pair = (current_type, required_type_class)
        if class_pair in COERCIBLE_TYPE_PAIRS:
            results_classes.append(real_required_type_class)
    return results_classes


def get_parent_key_or_index(input_data, variable_path):
    """Returns a tuple of parent, key_or_index

    Args:
        input_data (dict/list): the root data object that had an
                                ApiTypeException
        variable_path (list): the path to the exception, values are keys or
                              indices

    Returns:
        (parent, key_or_index):
            parent (dict/list): the parent of the item that has an
                                ApiTypeException
            key_or_index (str/int): the key that points to the item that has an
                                    ApiTypeException
    """
    current_item = input_data
    for index, path_value in enumerate(variable_path[:-1]):
        current_item = current_item[path_value]
    parent = current_item
    key_or_index = variable_path[-1]
    return parent, key_or_index


class OpenApiException(Exception):
    """The base exception class for all OpenAPIExceptions"""


class ApiTypeError(OpenApiException, TypeError):
    def __init__(self, required_types, current_item, path_to_item,
                 key_type=False):
        """ Raises an exception for TypeErrors

        Args:
            required_types (tuple): the primitive classes that current item
                                    should be an instance of
            current_item (any): the value which is the incorrect type
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
        """
        key_or_value = 'value'
        if key_type:
            key_or_value = 'key'
        msg = (
            "Invalid type for variable {0}. Required {1} type is {2} and "
            "passed type was {3} at location={4}".format(
                path_to_item[0],
                key_or_value,
                required_types,
                type(current_item),
                path_to_item
            )
        )
        super(ApiTypeError, self).__init__(msg)
        self.key_type = key_type
        self.path_to_item = path_to_item
        self.current_item = current_item
        self.required_types = required_types


class ApiValueError(OpenApiException, ValueError):
    def __init__(self, msg):
        super(ApiTypeError, self).__init__(msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg):
        super(ApiKeyError, self).__init__(msg)


def get_required_type_classes(required_types_mixed):
    """Converts the tuple required_types into a tuple of:
    tuple(child_classes), dict(class: required_type)
    where required_type is a class or list instance or dict instance

    Args:
        required_types_mixed (tuple/list): will contain either classes or instance
                                           of list or dict
    """
    results = []
    child_req_types_by_current_type = {}
    for required_type in required_types_mixed:
        if isinstance(required_type, list):
            results.append(list)
            child_req_types_by_current_type[list] = required_type[0]
        elif isinstance(required_type, dict):
            results.append(dict)
            child_req_types_by_current_type[dict] = required_type[str]
        else:
            results.append(required_type)
    return tuple(results), child_req_types_by_current_type


def change_keys_js_to_python(input_dict, model_class):
    """
    Converts from javascript_key keys in the input_dict to python_keys in
    the output dict using the mapping in model_class
    """

    output_dict = {}
    reversed_attr_map = {value: key for key, value in
                         six.iteritems(model_class.attribute_map)}
    for javascript_key, value in six.iteritems(input_dict):
        python_key = reversed_attr_map.get(javascript_key)
        if python_key is None:
            # if the key is unknown, it is in error or it is an
            # additionalProperties variable
            python_key = javascript_key
        output_dict[python_key] = value
    return output_dict


def validate_type(input_value, required_types_mixed, variable_path):
    """Raises a TypeError is there is a problem, otherwise continue

    :param input_value: any typed item
    :param required_types_mixed: For the response, a list of
        valid classes, or a list tuples of valid classes, or a dict where
        the value is a tuple of value classes.
    """
    results = get_required_type_classes(required_types_mixed)
    valid_classes, child_req_types_by_current_type = results

    valid_type = False
    for required_class in valid_classes:
        if ((type(input_value) == bool and required_class == int) or
                (type(input_value) == datetime and required_class == date)):
            # we can't use isinstance because
            # isinstance(True, int) == True == isinstance(datetime_val, date)
            valid_type = False
            continue
        valid_type = isinstance(input_value, required_class)
        if valid_type:
            break
    if not valid_type:
        raise ApiTypeError(
            valid_classes,
            input_value,
            variable_path
        )
    # input_value's type is in valid_classes
    if child_req_types_by_current_type == {}:
        # all types are of the required types and there are no more inner
        # variables left to look at
        return
    inner_required_types = child_req_types_by_current_type.get(
        type(input_value)
    )
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
                    key_type=True
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
                lambda item: (item[0],
                              model_to_dict(item[1], serialize=serialize))
                if hasattr(item[1], '_data_store') else item,
                value.items()
            ))
        elif hasattr(value, '_data_store'):
            result[attr] = model_to_dict(value, serialize=serialize)
        else:
            result[attr] = value

    return result
