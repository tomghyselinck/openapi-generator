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
from petstore_api.models.additional_properties_integer import AdditionalPropertiesInteger  # noqa: E501
from petstore_api.rest import ApiException
from test.utils import EXAMPLES, VAR_NAME_INVALID_TYPES, get_examples

ADDL_PROPS_VALUE_TYPE = 'int'
ADDL_PROPS_INVALID_VALUE_TYPES = [
    val for val in EXAMPLES.keys() if val != ADDL_PROPS_VALUE_TYPE
]


class TestAdditionalPropertiesInteger(unittest.TestCase):
    """AdditionalPropertiesInteger unit test stubs"""

    def test_addl_props_invalid_var_value_fails(self):
        for var_name in EXAMPLES['str']:
            var_values = get_examples(ADDL_PROPS_INVALID_VALUE_TYPES)
            for var_value in var_values:
                keyword_args = {var_name: var_value}
                with self.assertRaises(TypeError):
                    AdditionalPropertiesInteger(**keyword_args)

                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesInteger()
                    a[var_name] = var_value

    def test_addl_props_invalid_var_name_fails(self):
        var_names = get_examples(VAR_NAME_INVALID_TYPES)
        for var_name in var_names:
            for var_value in EXAMPLES['str']:
                with self.assertRaises(TypeError):
                    a = AdditionalPropertiesInteger()
                    a[var_name] = var_value

    def test_addl_props_valid_value_type_succeeds(self):
        for var_name in EXAMPLES['str']:
            for var_value in EXAMPLES[ADDL_PROPS_VALUE_TYPE]:
                keyword_args = {var_name: var_value}
                a = AdditionalPropertiesInteger(**keyword_args)
                b = AdditionalPropertiesInteger()
                b[var_name] = var_value
        assert True


if __name__ == '__main__':
    unittest.main()
