"""Validation schema for weather sensor data records."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class WeatherSensorData(BaseModel):
    """Schema for a single weather sensor reading and its metadata."""

    temperature_k: Optional[float]
    humidity: Optional[float]
    wind_speed_kph: Optional[float]
    wind_direction: Optional[float]
    pressure_pa: Optional[float]
    dew_point_k: Optional[float]
    heat_index_k: Optional[float]
    timestamp: Optional[datetime]
    sensor_id: Optional[str]
    location: Optional[str]
    battery_level: Optional[float]
    signal_strength: Optional[float]
    data_quality: Optional[bool]
    comments: Optional[str]
    sensor_type: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    firmware_version: Optional[str]
    calibration_data: Optional[str]
    raw_data: Optional[str]
    data_source: Optional[str]
    upload_time: Optional[str]
    upload_status: Optional[str]
    processing_notes: Optional[str]
    quality_flags: Optional[str]
    anomaly_detected: Optional[bool]
    anomaly_type: Optional[str]
    anomaly_severity: Optional[str]
    anomaly_timestamp: Optional[str]
    anomaly_resolution: Optional[str]
    anomaly_comments: Optional[str]
    sensor_status: Optional[str]
    sensor_location: Optional[str]
    sensor_calibration: Optional[str]
    sensor_accuracy: Optional[str]
    sensor_precision: Optional[str]

    @validator("timestamp", pre=True, always=True)
    def parse_timestamp(cls, value):
        """Ensure timestamp is parsed from ISO string if necessary."""
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                raise ValueError(f"Invalid ISO timestamp format: {value}")
        raise TypeError(f"Invalid type for timestamp: {type(value)}")
