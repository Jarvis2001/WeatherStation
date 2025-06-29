"""Generate a sample data record including base64-encoded images.

Used for populating the MongoDB during testing.

"""

import base64
from datetime import datetime, timezone
from pathlib import Path

from database.mongo_ops import WeatherDB


def encoded_image_to_base64(image_path: str) -> str:
    """Convert an image file to a base64-encoded string.

    Args:
        image_path (Path): Path to the image file.

    Returns:
        str: Base64-encoded string of the image.
    """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def create_sample_sensor_data():
    """Return a sample sensor data record including metadata and images."""
    return {
        "sensor_id": "ESP32-TEST-001",
        "location": "window-east",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "data_source": "iot",
        "readings": {
            "temperature_k": 298.15,
            "humidity": 45.0,
            "pressure_pa": 1013.25,
            "light_lux": 300.0,
            "wind_speed_kph": 12.4,
            "wind_direction": 135,
            "dew_point_k": 290.12,
            "heat_index_k": 302.5,
            "uv_index": 5.0,
        },
        "status": {
            "battery_level": 85,
            "signal_strength": -70,
            "firmware_version": "v1.2.3",
            "last_update": datetime.now(timezone.utc).isoformat(),
            "sensor_status": "active",
            "data_quality": True,
            "anomaly_detected": False,
            "last_communication": datetime.now(timezone.utc).isoformat(),
        },
        "metadata": {
            "sensor_type": "ESP32-WROOM",
            "firmware_version": "v1.5.0",
            "installation_date": datetime.now(timezone.utc).isoformat(),
            "maintenance_schedule": "2024-12-01T00:00:00Z",
            "location_description": "East-facing window sensor",
            "image_base64": encoded_image_to_base64(
                str(Path(__file__).parent / "sample_image.jpg")
            ),
            "image_format": "JPEG",
            "image_resolution": "1920x1080",
            "image_timestamp": datetime.now(timezone.utc).isoformat(),
            "image_description": "Sample image captured by the sensor",
            "image_checksum": "abc123def456",
            "image_size_bytes": 204800,  # Example size in bytes
            "image_orientation": "landscape",
            "image_camera_model": "ESP32-CAM",
            "image_capture_mode": "auto",
            "image_exposure_time": "1/60",
            "image_iso": 100,
            "image_white_balance": "auto",
            "image_color_space": "sRGB",
            "image_compression": "JPEG",
            "image_quality": "high",
            "image_timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "image_latitude": 37.7749,
            "image_longitude": -122.4194,
            "image_altitude": 30.0,
            "image_orientation_angle": 0,
            "image_gps_accuracy": 5.0,
            "image_gps_timestamp": datetime.now(timezone.utc).isoformat(),
            "image_gps_status": "valid",
            "image_gps_satellites": 8,
            "image_gps_hdop": 1.0,
            "image_gps_pdop": 1.5,
            "image_gps_vdop": 1.2,
            "image_gps_geoid_separation": 0.0,
            "image_gps_age": 0,
            "image_gps_dop": 1.0,
            "image_gps_speed": 0.0,
            "image_gps_course": 0.0,
            "image_gps_fix_type": "3D",
            "image_gps_fix_quality": "high",
            "image_gps_satellite_ids": [1, 2, 3, 4, 5, 6, 7, 8],
            "image_gps_positioning_system": "GPS",
            "image_gps_positioning_system_version": "v2.0",
            "image_gps_positioning_system_accuracy": 5.0,
            "image_gps_positioning_system_timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "image_gps_positioning_system_status": "active",
            "image_gps_positioning_system_signal_strength": -70,
            "image_gps_positioning_system_last_update": datetime.now(
                timezone.utc
            ).isoformat(),
            "image_gps_positioning_system_calibration": "calibrated",
            "image_gps_positioning_system_calibration_date": datetime.now(
                timezone.utc
            ).isoformat(),
            "image_gps_positioning_system_calibration_status": "valid",
            "image_gps_positioning_system_calibration_quality": "high",
            "image_gps_positioning_system_calibration_accuracy": 5.0,
            "image_gps_positioning_system_calibration_timestamp": datetime.now(
                timezone.utc
            ).isoformat(),
            "upload_status": "Success",
            "comments": "This is a sample image for testing purposes.",
            "tags": ["sample", "test", "sensor"],
            "calibration_date": datetime.now(timezone.utc).isoformat(),
        },
        "cloud_snapshot": {
            "image_base64": encoded_image_to_base64(
                str(Path(__file__).parent / "sample_cloud_image.jpg")
            ),
            "image_format": "JPEG",
            "image_resolution": "1920x1080",
            "image_timestamp": datetime.now(timezone.utc).isoformat(),
            "image_description": "Sample cloud image captured by the sensor",
            "image_checksum": "def456abc123",
            "image_size_bytes": 204800,  # Example size in bytes
            "filename": "cloud_snapshot_001.jpg",
            "annotated": True,
            "labels": ["cloud", "weather"],
            "annotations": {
                "cloud_type": "cumulus",
                "cloud_cover_percentage": 75,
                "cloud_height_meters": 1500,
                "cloud_base_meters": 1200,
                "cloud_top_meters": 1800,
                "visibility_km": 10.0,
                "weather_conditions": "partly cloudy",
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
            "upload_status": "Success",
            "comments": "This is a sample cloud image for testing purposes.",
            "tags": ["cloud", "weather", "sample"],
            "vision_ai_score": None,
            "vision_ai_model": None,
        },
    }


if __name__ == "__main__":
    sample_data = create_sample_sensor_data()
    db = WeatherDB()
    db.insert_sensor_data(cleaned_data=sample_data)
    print("Sample sensor data inserted into MongoDB.")
