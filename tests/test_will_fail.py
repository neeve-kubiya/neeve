def test_this_will_fail():
    """This test is designed to always fail"""
    assert False, "This test is designed to fail for testing PR failure notifications"

def test_this_will_also_fail():
    """Another failing test"""
    expected = 42
    actual = 24
    assert expected == actual, f"Expected {expected} but got {actual}" 