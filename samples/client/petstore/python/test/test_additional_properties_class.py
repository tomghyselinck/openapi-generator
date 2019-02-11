# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import petstore_api
from petstore_api.models.additional_properties_class import AdditionalPropertiesClass  # noqa: E501
from petstore_api.rest import ApiException
from test.utils import EXAMPLES, get_examples

class TestAdditionalPropertiesClass(unittest.TestCase):
    """AdditionalPropertiesClass unit test stubs"""

    def test_map_string_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'str'
        ]
        var_values = get_examples(invalid_value_types)
        for var_name in EXAMPLES['str']:
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_string={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_string'] = {var_name: var_value}

    def test_map_string_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['str']:
                a = AdditionalPropertiesClass(
                    map_string={var_name: var_value},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_string'] = {var_name: var_value}
        assert True

    def test_map_number_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'float'
        ]
        for var_name in EXAMPLES['str']:
            var_values = get_examples(invalid_value_types)
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_number={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_number'] = {var_name: var_value}

    def test_map_number_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['float']:
                a = AdditionalPropertiesClass(
                    map_number={var_name: var_value},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_number'] = {var_name: var_value}
        assert True

    def test_map_integer_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'int'
        ]
        for var_name in EXAMPLES['str']:
            var_values = get_examples(invalid_value_types)
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_integer={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_integer'] = {var_name: var_value}

    def test_map_integer_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['int']:
                a = AdditionalPropertiesClass(
                    map_integer={var_name: var_value},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_integer'] = {var_name: var_value}
        assert True

    def test_map_boolean_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'bool'
        ]
        for var_name in EXAMPLES['str']:
            var_values = get_examples(invalid_value_types)
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_boolean={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_boolean'] = {var_name: var_value}

    def test_map_boolean_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['bool']:
                a = AdditionalPropertiesClass(
                    map_boolean={var_name: var_value},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_boolean'] = {var_name: var_value}
        assert True

    def test_map_array_integer_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'int'
        ]
        examples = get_examples(invalid_value_types)
        var_values = [[example] for example in examples]
        # add arrays with mixed types, some valid + invalid
        for example in examples:
            var_values.append([1, 2, example])
        for var_name in EXAMPLES['str']:
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_array_integer={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_array_integer'] = {var_name: var_value}

    def test_map_array_integer_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['int']:
                a = AdditionalPropertiesClass(
                    map_array_integer={var_name: [var_value]},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_array_integer'] = {var_name: [var_value]}
        assert True

    def test_map_array_anytype_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'list'
        ]
        for var_name in EXAMPLES['str']:
            var_values = get_examples(invalid_value_types)
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    AdditionalPropertiesClass(
                        map_array_anytype={var_name: var_value},
                        _check_type=True
                    )

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a['map_array_anytype'] = {var_name: var_value}

    def test_map_array_anytype_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES['list']:
                a = AdditionalPropertiesClass(
                    map_array_anytype={var_name: var_value},
                    _check_type=True
                )
                b = AdditionalPropertiesClass(_check_type=True)
                b['map_array_anytype'] = {var_name: var_value}
        assert True

    def test_map_map_string_invalid_var_value_fails(self):
        invalid_value_types = [
            val for val in EXAMPLES.keys() if val != 'str'
        ]
        var_values = get_examples(invalid_value_types)
        for var_name in EXAMPLES['str']:
            for var_key in EXAMPLES['str']:
                for var_value in var_values:
                    with self.assertRaises(TypeError):
                        AdditionalPropertiesClass(
                            map_map_string={var_name: {var_key: var_value}},
                            _check_type=True
                        )

                    with self.assertRaises(TypeError):
                        a = AdditionalPropertiesClass(_check_type=True)
                        a['map_map_string'] = {var_name: {var_key: var_value}}
        # add dict with mixed types, some valid + invalid
        for var_value in var_values:
            with self.assertRaises(TypeError):
                AdditionalPropertiesClass(
                    map_map_string={
                        'a': {
                            'b': 'e',
                            'c': 'f',
                            'd': var_value
                        }
                    },
                    _check_type=True
                )

    def test_map_map_string_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_key in EXAMPLES['str']:
                for var_value in EXAMPLES['str']:
                    a = AdditionalPropertiesClass(
                        map_map_string={var_name: {var_key: var_value}},
                        _check_type=True
                    )
                    b = AdditionalPropertiesClass(_check_type=True)
                    b['map_map_string'] = {var_name: {var_key: var_value}}
        assert True

    def test_map_map_anytype_invalid_var_value_fails(self):
        invalid_value_types = ['None']
        for var_name in EXAMPLES['str']:
            for var_key in EXAMPLES['str']:
                var_values = get_examples(invalid_value_types)
                for var_value in var_values:
                    with self.assertRaises(TypeError):
                        AdditionalPropertiesClass(
                            map_map_anytype={var_name: {var_key: var_value}},
                            _check_type=True
                        )

                    with self.assertRaises(TypeError):
                        a = AdditionalPropertiesClass(_check_type=True)
                        a['map_map_anytype'] = {var_name: {var_key: var_value}}

    def test_map_map_anytype_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_key in EXAMPLES['str']:
                for var_value in EXAMPLES['dict']:
                    a = AdditionalPropertiesClass(
                        map_map_anytype={var_name: {var_key: var_value}},
                        _check_type=True
                    )
                    b = AdditionalPropertiesClass(_check_type=True)
                    b['map_map_anytype'] = {var_name: {var_key: var_value}}
        assert True

    def test_anytypes_invalid_var_value_fails(self):
        invalid_value_types = ['None']
        anytype_vars = ['anytype_1', 'anytype_2', 'anytype_2']
        for anytype_var in anytype_vars:
            var_values = get_examples(invalid_value_types)
            for var_value in var_values:
                with self.assertRaises(TypeError):
                    keyword_args = {
                        anytype_var: var_value,
                        '_check_type': True
                    }
                    AdditionalPropertiesClass(**keyword_args)

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesClass(_check_type=True)
                    a[anytype_var] = var_value

    def test_anytypes_valid_value_type_succeeds(self):
        anytype_vars = ['anytype_1', 'anytype_2', 'anytype_2']
        valid_value_types = [
            val for val in EXAMPLES.keys() if val != 'None'
        ]
        for anytype_var in anytype_vars:
            for var_value in get_examples(valid_value_types):
                keyword_args = {
                    anytype_var: var_value,
                    '_check_type': True
                }
                a = AdditionalPropertiesClass(**keyword_args)
                b = AdditionalPropertiesClass(_check_type=True)
                b[anytype_var] = var_value
        assert True


if __name__ == '__main__':
    unittest.main()
