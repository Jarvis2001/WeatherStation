"""# SPDX-License-Identifier: Apache-2.0.

UploadMetadata Schema:

This module defines the UploadMetadata schema using Pydantic, which represents metadata and diagnostic information about
an upload process. It includes fields for timestamps, status, source, data quality, comments,
raw data, data source, upload status, processing notes, quality flags, error logs, warnings, debug information,
and processing time.
"""

from typing import Optional

from pydantic import BaseModel, Field, datetime


class UploadMetadata(BaseModel):
    """Represents metadata and diagnostic information about an upload process.

    Contains fields for timestamps, status, source, data quality, comments,
    raw data, data source, upload status, processing notes, quality flags, error logs,
    warnings, debug information, and processing time.

    Attributes:
        timestamp (Optional[datetime]): Time when the upload was initiated.
        upload_time (Optional[datetime]): Time when the upload was completed.
        status (Optional[str]): Status of the upload (e.g. "success", "failed").
        source (Optional[str]): Source of the data being uploaded.
        data_quality (Optional[bool]): Indicates if the data quality is acceptable.
        comments (Optional[str]): Additional comments about the upload.
        raw_data (Optional[str]): Raw data associated with the upload.
        data_source (Optional[str]): Identifier for the data source.
        upload_status (Optional[str]): Status of the upload process.
        processing_notes (Optional[str]): Notes generated during processing.
        quality_flags (Optional[str]): Flags indicating data quality issues.
        error_logs (Optional[str]): Raw error logs from failed uploads.
        warnings (Optional[str]): Non-critical warnings during processing.
        debug_info (Optional[str]): Supplementary debug info for development.
        processing_time (Optional[float]): Time taken to process the upload in seconds.
        upload_id (Optional[str]): Unique identifier for the upload.
    """

    timestamp: Optional[datetime]
    upload_time: Optional[datetime]
    status: Optional[str]
    source: Optional[str]
    data_quality: Optional[bool]
    comments: Optional[str]
    raw_data: Optional[str]
    data_source: Optional[str]
    upload_status: Optional[str]
    processing_notes: Optional[str]
    quality_flags: Optional[str]
    error_logs: Optional[str]
    warnings: Optional[str]
    debug_info: Optional[str]
    processing_time: Optional[float] = Field(
        default=None, description="Time taken to process the upload in seconds"
    )
    upload_id: Optional[str] = Field(
        default=None, description="Unique identifier for the upload"
    )
