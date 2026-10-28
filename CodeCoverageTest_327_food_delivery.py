import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time

# --- delivery_charge ---

def test_nearby_small_order():
    assert delivery_charge(2, 200, False) == 20

def test_out_of_range_zero():
    with pytest.raises(ValueError):
        delivery_charge(0, 200, False)

def test_out_of_range_too_far():
    with pytest.raises(ValueError):
        delivery_charge(16, 200, False)

def test_free_delivery_high_value():
    assert delivery_charge(5, 500, False) == 0

def test_mid_distance():
    assert delivery_charge(5, 200, False) == 40

def test_long_distance():
    assert delivery_charge(12, 200, False) == 60

def test_rain_surcharge():
    assert delivery_charge(2, 200, True) == 50  # 20 + 30

# --- apply_coupon ---

def test_no_coupon():
    assert apply_coupon(300, None, False) == 300

def test_invalid_coupon():
    with pytest.raises(ValueError):
        apply_coupon(300, "FAKE", False)

def test_welcome_not_first_order():
    with pytest.raises(ValueError):
        apply_coupon(300, "WELCOME", False)

def test_order_below_minimum():
    assert apply_coupon(100, "SAVE50", True) == 100

def test_save50_coupon():
    assert apply_coupon(300, "SAVE50", False) == 250

def test_welcome_coupon_first_order():
    assert apply_coupon(300, "WELCOME", True) == 200

# --- estimated_time ---

def test_basic_time():
    assert estimated_time(5, False, False) == 35  # 15 + 20

def test_peak_hour():
    assert estimated_time(5, True, False) == 45  # 15 + 20 + 10

def test_restaurant_busy():
    assert estimated_time(5, False, True) == 50  # 15 + 20 + 15

def test_peak_and_busy():
    assert estimated_time(5, True, True) == 60  # 15 + 20 + 10 + 15 + 5 - wait, 65