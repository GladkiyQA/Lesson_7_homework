from Main_page_1 import Fillng_form

fill_form = Fillng_form()
def test_main_page():
    fill_form.open_page()
    fill_form.filling_out_the_form()
    a = fill_form.getting_values_for_zip()
    b = fill_form.getting_values_for_other_fields()
    assert 'alert-success' in b and 'alert-danger' in a
