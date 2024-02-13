from qwerty import SlowCalculator

slow_calculator = SlowCalculator()

def test_slow_calculator():
    slow_calculator.open_page()
    slow_calculator.delay_form("18")
    slow_calculator.click_button("7")
    slow_calculator.click_button("-")
    slow_calculator.click_button("3")
    slow_calculator.click_button("=")
    a = slow_calculator.get_result("4")
    assert "4" == a