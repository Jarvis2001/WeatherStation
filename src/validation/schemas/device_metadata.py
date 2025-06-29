"""Defines data models for validating and handling sensor device metadata.

This module contains Pydantic models used to represent device-level information
for sensor nodes in a weather monitoring or edge computing system. It provides
structured fields for recording identity, hardware specs, calibration, and
connectivity details.

Intended for use with data ingestion, validation, and logging workflows.
"""

from typing import Optional

from pydantic import BaseModel


class DeviceMetadata(BaseModel):
    """Metadata describing a sensor device's hardware and telemetry details.

    Captures key attributes of a sensor device such as its identity, configuration,
    calibration status, and hardware information. Useful for validating, logging, or
    storing device-specific context alongside sensor measurements.

    Attributes:
        sensor_id (Optional[str]): Unique identifier of the sensor device.
        location (Optional[str]): Description of the sensor's deployment location.
        battery_level (Optional[float]): Remaining battery percentage (0-100).
        signal_strength (Optional[float]): Wireless signal strength in dBm.
        sensor_type (Optional[str]): Type or model of the sensor used.
        manufacturer (Optional[str]): Name of the hardware vendor or maker.
        model (Optional[str]): Model name or number of the device.
        firmware_version (Optional[str]): Installed firmware version of the sensor.
        calibration_data (Optional[str]): Any raw calibration reference data.
        sensor_status (Optional[str]): Reported operational status (e.g., 'ok', 'faulty').
        sensor_location (Optional[str]): Physical mount point or zone inside the device.
        sensor_calibration (Optional[str]): Summary or tag for calibration state.
        sensor_accuracy (Optional[str]): Manufacturer-quoted or estimated accuracy.
        sensor_precision (Optional[str]): Precision or resolution of readings.
    """

    sensor_id: Optional[str]
    location: Optional[str]
    battery_level: Optional[float]
    signal_strength: Optional[float]
    sensor_type: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    firmware_version: Optional[str]
    calibration_data: Optional[str]
    sensor_status: Optional[str]
    sensor_location: Optional[str]
    sensor_calibration: Optional[str]
    sensor_accuracy: Optional[str]
    sensor_precision: Optional[str]
