"""# SPDX-License-Identifier: Apache-2.0.

WeatherDB Test Suite:

This module contains tests for the WeatherDB class, which handles MongoDB operations for weather sensor data
and image metadata. It uses pytest for testing and pymongo for database interactions.

"""

from datetime import datetime
from json import ObjectId

import pytest

from database.mongo_ops import WeatherDB


@pytest.fixture(scope="module")
def test_db():
    """Fixture to create a test database instance for WeatherDB."""
    return WeatherDB(
        db_name="weather_station_test"
    )  # Use a test database to avoid affecting production data


def test_insert_sensor_data_basic(test_db):
    """Test inserting basic sensor data into the database."""
    sample = {
        "_id": ObjectId(),
        "timestamp": "2025-06-29T14:00:00Z",
        "sensor_id": "esp32_01",
        "location": {"lat": 28.6139, "lon": 77.2090, "description": "My window, Delhi"},
        "readings": {
            "temperature_c": 36.5,
            "humidity_percent": 64.2,
            "pressure_hpa": 1008.3,
            "wind_speed_mps": 3.2,
            "wind_direction_deg": 120,
            "rain_mm": 0.0,
            "sunlight_lux": 12000,
            "dew_point_c": 28.4,
            "heat_index_c": 40.1,
        },
        "image": {
            "base64_data": "<BASE64_IMAGE_DATA>",
            "format": "jpeg",
            "width": 640,
            "height": 480,
        },
        "device_info": {
            "battery_level": 82,
            "signal_strength": -70,
            "sensor_type": "dht22 + anemometer",
            "firmware_version": "v1.2.3",
            "model": "ESP32-CAM",
        },
        "anomaly": {
            "detected": False,
            "type": None,
            "severity": None,
            "comments": None,
        },
        "validation": {
            "quality_flags": ["sensor_check_passed", "image_valid"],
            "data_quality": "good",
            "validator_version": "1.0.0",
        },
        "upload": {
            "status": "success",
            "upload_time": "2025-06-29T14:01:22Z",
            "source": "local_secure_transfer",
        },
        "logs": {
            "processing_notes": "No issues. Cleaned and validated.",
            "raw_data": "<OPTIONAL_RAW_JSON>",
        },
    }

    test_db.insert_sensor_data(sample)
    result = test_db.sensor_collection.find_one({"sensor_id": "esp32_01"})
    assert result is not None
    assert result["sensor_id"] == "esp32_01"
    assert "readings" in result
    assert result["readings"]["temperature_c"] == 36.5


def test_insert_image_metadata(test_db):
    """Test inserting image metadata into the database."""
    image_data = {
        "_id": ObjectId(),
        "timestamp": "2025-06-29T14:00:00Z",
        "sensor_id": "esp32_01",
        "image": {
            "base64_data": "<BASE64_IMAGE_DATA>",
            "format": "jpeg",
            "width": 640,
            "height": 480,
        },
        "location": {"lat": 28.6139, "lon": 77.2090, "description": "My window, Delhi"},
    }
    test_db.insert_cloud_image_metadata(image_data)
    result = test_db.image_collection.find_one({"sensor_id": "esp32_01"})
    assert result is not None
    assert result["image"]["format"] == "jpeg"


def test_timestamp_parsing(test_db):
    """Test that timestamps are correctly parsed and stored in the database."""
    sample = {"timestamp": "2025-06-29T10:00:00"}
    test_db.insert_sensor_data(sample)
    result = test_db.sensor_collection.find_one(
        {"timestamp": datetime(2025, 6, 29, 10, 0)}
    )
    assert result is not None


def teardown_module(module):
    """Teardown function to clean up the test database after all tests."""
    db = WeatherDB(
        db_name="weather_station_test"
    )  # Clean up the test database after tests
    db.sensor_collection.drop()
    db.image_collection.drop()
