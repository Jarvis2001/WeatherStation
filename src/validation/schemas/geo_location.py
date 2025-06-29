"""# SPDX-License-Identifier: Apache-2.0.

GeoLocation Schema:

This module defines the GeoLocation schema using Pydantic, which represents geographical location data.
It includes fields for latitude, longitude, altitude, accuracy, timestamps, and various metadata.

"""

from typing import Optional

from pydantic import BaseModel


class GeoLocation(BaseModel):
    """Represents geographical location data.

    Contains fields for latitude, longitude, altitude, accuracy, timestamps, and various metadata.

    Attributes:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        description (Optional[str]): Description of the location.
        altitude (Optional[float]): Altitude in meters.
        accuracy (Optional[float]): Accuracy of the location in meters.
        timestamp (Optional[str]): Timestamp in ISO 8601 format.
        source (Optional[str]): Source of the location data (e.g., GPS, WiFi).
        device_id (Optional[str]): ID of the device that captured the location.
        location_type (Optional[str]): Type of location (e.g., home, work, outdoor).
        additional_info (Optional[str]): Any additional information about the location.
        processing_notes (Optional[str]): Notes on how the location data was processed.
        error_logs (Optional[str]): Any errors encountered during processing.
        warnings (Optional[str]): Warnings encountered during processing.
        debug_info (Optional[str]): Debug information for troubleshooting.
        processing_time (Optional[float]): Time taken to process the location data in seconds.
        upload_time (Optional[str]): Time when the location data was uploaded.
        upload_status (Optional[str]): Status of the upload (e.g., success, failure).
        location_accuracy (Optional[str]): Accuracy of the location data (e.g., high, medium, low).
        location_precision (Optional[str]): Precision of the location data.
    """

    lat: float
    lon: float
    description: Optional[str]
    altitude: Optional[float] = None  # Altitude in meters
    accuracy: Optional[float] = None  # Accuracy in meters
    timestamp: Optional[str] = None  # ISO 8601 format
    source: Optional[str] = None  # Source of the location data (e.g., GPS, WiFi)
    device_id: Optional[str] = None  # ID of the device that captured the location
    location_type: Optional[str] = None  # Type of location (e.g., home, work, outdoor)
    additional_info: Optional[str] = (
        None  # Any additional information about the location
    )
    processing_notes: Optional[str] = (
        None  # Notes on how the location data was processed
    )
    error_logs: Optional[str] = None  # Any errors encountered during processing
    warnings: Optional[str] = None  # Warnings encountered during processing
    debug_info: Optional[str] = None  # Debug information for troubleshooting
    processing_time: Optional[float] = (
        None  # Time taken to process the location data in seconds
    )
    upload_time: Optional[str] = None  # Time when the location data was uploaded
    upload_status: Optional[str] = None  # Status of the upload (e.g.,success, failure)
    location_accuracy: Optional[str] = (
        None  # Accuracy of the location data (e.g., high, medium, low)
    )
    location_precision: Optional[str] = None  # Precision of the location data (e.g
