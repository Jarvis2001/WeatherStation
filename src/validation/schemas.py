"""Validation schema for weather sensor data records."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, StrictFloat, StrictStr, validator


class WeatherSensorData(BaseModel):
    """Schema for a single weather sensor reading and its metadata."""

    temperature_k: Optional[StrictFloat] = Field(
        None, ge=0, description="Temperature in Kelvin"
    )
    humidity: Optional[StrictFloat] = Field(
        None, ge=0, le=100, description="Humidity percentage"
    )
    wind_speed_kph: Optional[StrictFloat] = Field(
        None, ge=0, description="Wind speed in kilometers per hour"
    )
    wind_direction: Optional[StrictFloat] = Field(
        None, ge=0, le=360, description="Wind direction in degrees"
    )
    pressure_pa: Optional[StrictFloat] = Field(
        None, ge=0, description="Atmospheric pressure in Pascals"
    )
    dew_point_k: Optional[StrictFloat] = Field(
        None, ge=0, description="Dew point in Kelvin"
    )
    heat_index_k: Optional[StrictFloat] = Field(
        None, ge=0, description="Heat index in Kelvin"
    )

    timestamp: Optional[datetime]
    upload_time: Optional[datetime]
    anomaly_timestamp: Optional[datetime]

    sensor_id: Optional[StrictStr]
    location: Optional[StrictStr]
    battery_level: Optional[StrictFloat]
    signal_strength: Optional[StrictFloat]
    data_quality: Optional[bool]

    comments: Optional[StrictStr]
    sensor_type: Optional[StrictStr]
    manufacturer: Optional[StrictStr]
    model: Optional[StrictStr]
    firmware_version: Optional[StrictStr]
    calibration_data: Optional[StrictStr]
    raw_data: Optional[StrictStr]
    data_source: Optional[StrictStr]

    upload_status: Optional[StrictStr]
    processing_notes: Optional[StrictStr]
    quality_flags: Optional[StrictStr]

    anomaly_detected: Optional[bool]
    anomaly_type: Optional[StrictStr]
    anomaly_severity: Optional[StrictStr]
    anomaly_timestamp: Optional[datetime]
    anomaly_resolution: Optional[StrictStr]
    anomaly_comments: Optional[StrictStr]

    sensor_status: Optional[StrictStr]
    sensor_location: Optional[StrictStr]
    sensor_calibration: Optional[StrictStr]
    sensor_accuracy: Optional[StrictStr]
    sensor_precision: Optional[StrictStr]

    # Validators
    @validator("timestamp", "upload_time", "anomaly_timestamp", pre=True, always=True)
    def parse_iso_datetime(cls, value):
        """Ensure timestamps are parsed from ISO strings if necessary."""
        if value is None or isinstance(value, datetime):
            return value
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                raise ValueError(f"Invalid ISO timestamp format: {value}")
        raise TypeError(f"Invalid type for datetime field: {type(value)}")
