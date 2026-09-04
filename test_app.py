from app import calculate_quote

def test_basic_quote_adult():
    quote = calculate_quote(30, "basic")
    assert quote == 50.0

def test_standard_quote_adult():
    quote = calculate_quote(30, "standard")
    assert quote == 75.0

def test_premium_quote_young():
    quote = calculate_quote(22, "premium")
    assert quote == 150.0

def test_basic_quote_senior():
    quote = calculate_quote(60, "basic")
    assert quote == 65.0

def test_unknown_coverage_defaults_to_basic_multiplier():
    quote = calculate_quote(30, "unknown_type")
    assert quote == 50.0
