import pytest
from transform.clean_sensor import clean_sensor_data


def test_temperature_conversion():
    input_data = {"temperature_c": 25}
    result = clean_sensor_data(input_data)
    assert result["temperature_k"] == pytest.approx(298.15, rel=1e-5)


def test_humidity_conversion():
    input_data = {"humidity": "80"}
    result = clean_sensor_data(input_data)
    assert result["humidity"] == 80.0


def test_wind_speed_conversion():
    input_data = {"wind_speed_mps": 10}
    result = clean_sensor_data(input_data)
    assert result["wind_speed_kph"] == pytest.approx(36.0, rel=1e-5)


def test_boolean_conversion():
    input_data = {"anamoly_detected": "True"}
    result = clean_sensor_data(input_data)
    assert result["anomaly_detected"] is True
