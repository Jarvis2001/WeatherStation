"""# SPDX-License-Identifier: Apache-2.0.

ImageInfo Schema:

This module defines the ImageInfo schema using Pydantic, which represents metadata and diagnostic information about
an image capture. It includes fields for image dimensions, format details, timestamps, and optional diagnostics.

"""

from typing import Optional

from pydantic import BaseModel


class ImageInfo(BaseModel):
    """Represents metadata and diagnostic information about an image capture.

    Contains image dimensions, format details, timestamps, and optional diagnostics
    such as error logs, warnings, and processing duration.

    Attributes:
        base64_data (str): Base64-encoded representation of the image.
        width (Optional[int]): Width of the image in pixels.
        height (Optional[int]): Height of the image in pixels.
        resolution (Optional[str]): Human-readable resolution description (e.g. "640x480").
        format (Optional[str]): Image format, such as 'jpeg' or 'png'.
        timestamp (Optional[str]): Capture time in ISO 8601 format.
        description (Optional[str]): Description of the image content or context.
        camera_model (Optional[str]): Model or identifier of the camera used.
        location (Optional[str]): Human-readable location description or coordinates.
        device_id (Optional[str]): ID of the device that captured the image.
        upload_time (Optional[str]): Time when the image was uploaded.
        upload_status (Optional[str]): Status of the upload (e.g. "success", "failed").
        processing_notes (Optional[str]): Notes generated during image processing.
        error_logs (Optional[str]): Raw error logs from failed processing attempts.
        warnings (Optional[str]): Non-critical processing warnings.
        debug_info (Optional[str]): Supplementary debug info for development.
        processing_time (Optional[float]): Time taken to process the image, in seconds.
    """

    base64_data: str
    width: Optional[int] = None
    height: Optional[int] = None
    resolution: Optional[str] = None
    format: Optional[str] = None
    timestamp: Optional[str] = None
    description: Optional[str] = None
    camera_model: Optional[str] = None
    location: Optional[str] = None
    device_id: Optional[str] = None
    upload_time: Optional[str] = None
    upload_status: Optional[str] = None
    processing_notes: Optional[str] = None
    error_logs: Optional[str] = None
    warnings: Optional[str] = None
    debug_info: Optional[str] = None
    processing_time: Optional[float] = None
