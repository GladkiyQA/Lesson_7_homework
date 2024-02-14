from Main_page_1 import Fillng_form
import pytest

fill_form = Fillng_form()
def test_main_page_1():
    fill_form.open_page()
    fill_form.filling_out_the_form()
    a = fill_form.getting_values_for_zip()
    assert 'alert-danger' in a


@pytest.mark.parametrize("expected_class", ["alert-success"])
def test_fields_have_expected_class(expected_class):
    fill_form.open_page()
    fill_form.filling_out_the_form()
    field_values = fill_form.getting_values_for_other_fields()

    for value in field_values:
        assert expected_class in value, f"Expected class '{expected_class}' not found in field values: {field_values}"

