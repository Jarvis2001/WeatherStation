"""# SPDX-License-Identifier: Apache-2.0.

WeatherSensorData Schema:

This module defines the WeatherSensorData schema using Pydantic, which represents metadata and diagnostic information
about weather sensor data. It includes fields for timestamps, sensor ID, location, readings, image information,
device metadata, anomaly information, validation details, upload metadata, log metadata, and various optional fields
for additional information.

"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .anomaly_info import AnomalyInfo
from .device_metadata import DeviceMetadata
from .geo_location import GeoLocation
from .image_info import ImageInfo
from .log_metadata import LogMetadata
from .sensor_reading import SensorReading
from .upload_metadata import UploadMetadata
from .validation_info import ValidationInfo


class WeatherSensorData(BaseModel):
    """Represents metadata and diagnostic information about weather sensor data.

    Contains fields for timestamps, sensor ID, location, readings, image information,
    device metadata, anomaly information, validation details, upload metadata, log metadata,
    and various optional fields for additional information.

    Attributes:
        timestamp (datetime): Timestamp of the sensor data.
        sensor_id (str): Unique identifier for the sensor.
        location (GeoLocation): Geographical location of the sensor.
        readings (SensorReading): Sensor readings including temperature, humidity, etc.
        image (Optional[ImageInfo]): Optional image information associated with the sensor data.
        device_info (DeviceMetadata): Metadata about the device that collected the data.
        anomaly (Optional[AnomalyInfo]): Optional anomaly information detected in the sensor data.
        validation (Optional[ValidationInfo]): Optional validation information for the sensor data.
        upload (Optional[UploadMetadata]): Optional metadata about the upload process.
        logs (Optional[LogMetadata]): Optional log metadata associated with the sensor data.
        comments (Optional[str]): Additional comments about the sensor data.
        data_quality (Optional[bool]): Indicates if the data quality is acceptable.
        processing_time (Optional[float]): Time taken to process the sensor data in seconds.
        source (Optional[str]): Source of the sensor data.
        status (Optional[str]): Status of the sensor data (e.g., "success", "
        failure").
        upload_status (Optional[str]): Status of the upload process (e.g., "pending",
        "completed", "failed").
        additional_info (Optional[str]): Any additional information about the sensor data.
        error_logs (Optional[str]): Any errors encountered during processing.
        warnings (Optional[str]): Warnings encountered during processing.
        debug_info (Optional[str]): Debug information for troubleshooting.
        processing_notes (Optional[str]): Notes on how the data was processed.
        upload_time (Optional[datetime]): Time when the data was uploaded.
        validation_status (Optional[str]): Status of the validation (e.g., "valid", "
        "invalid", "pending").
        validation_notes (Optional[str]): Notes on the validation process.
        validation_errors (Optional[str]): Errors encountered during validation.
        validation_warnings (Optional[str]): Warnings encountered during validation.
        validation_debug_info (Optional[str]): Debug information for validation.
        validation_processing_time (Optional[float]): Time taken to validate the data in seconds.
        validation_upload_time (Optional[datetime]): Time when the validation data was uploaded.
        validation_upload_status (Optional[str]): Status of the validation upload (e.g., "success
        ", "failure").
        validation_location (Optional[GeoLocation]): Location associated with the validation.
        validation_image (Optional[ImageInfo]): Image associated with the validation.
        validation_device_info (Optional[DeviceMetadata]): Device information associated with the validation.
        validation_anomaly (Optional[AnomalyInfo]): Anomaly information associated with the validation.
        validation_comments (Optional[str]): Comments on the validation process.
        validation_data_quality (Optional[bool]): Data quality assessment for the validation.
        validation_source (Optional[str]): Source of the validation data.
        validation_status (Optional[str]): Status of the validation (e.g., "valid", "invalid").
    """

    timestamp: datetime
    sensor_id: str
    location: GeoLocation
    readings: SensorReading
    image: Optional[ImageInfo]
    device_info: DeviceMetadata
    anomaly: Optional[AnomalyInfo]
    validation: Optional[ValidationInfo]
    upload: Optional[UploadMetadata]
    logs: Optional[LogMetadata]
    comments: Optional[str] = None
    data_quality: Optional[bool] = None
    processing_time: Optional[float] = None
    source: Optional[str] = None
    status: Optional[str] = None  # e.g., "success", "failure"
    upload_status: Optional[str] = None  # e.g., "pending", "completed", "failed"
    additional_info: Optional[str] = None  # Any additional information about the data
    error_logs: Optional[str] = None  # Any errors encountered during processing
    warnings: Optional[str] = None  # Warnings encountered during processing
    debug_info: Optional[str] = None  # Debug information for troubleshooting
    processing_notes: Optional[str] = None  # Notes on how the data was processed
    upload_time: Optional[datetime] = None  # Time when the data was uploaded
    validation_status: Optional[str] = None  # e.g., "valid", "invalid", "pending"
    validation_notes: Optional[str] = None  # Notes on the validation process
    validation_errors: Optional[str] = None  # Errors encountered during validation
    validation_warnings: Optional[str] = None  # Warnings encountered during validation
    validation_debug_info: Optional[str] = None  # Debug information for validation
    validation_processing_time: Optional[float] = (
        None  # Time taken to validate the data in seconds
    )
    validation_upload_time: Optional[datetime] = (
        None  # Time when the validation data was uploaded
    )
    validation_upload_status: Optional[str] = (
        None  # Status of the validation upload (e.g., success, failure)
    )
    validation_location: Optional[GeoLocation] = (
        None  # Location associated with the validation
    )
    validation_image: Optional[ImageInfo] = None  # Image associated with the validation
    validation_device_info: Optional[DeviceMetadata] = (
        None  # Device information associated with the validation
    )
    validation_anomaly: Optional[AnomalyInfo] = None  # Anomaly information associated
    validation_comments: Optional[str] = None  # Comments on the validation process
    validation_data_quality: Optional[bool] = (
        None  # Data quality assessment for the validation
    )
    validation_source: Optional[str] = None  # Source of the validation data
    validation_status: Optional[str] = (
        None  # Status of the validation (e.g., "valid", "invalid")
    )
