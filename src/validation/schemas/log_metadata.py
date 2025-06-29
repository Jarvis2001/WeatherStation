"""# SPDX-License-Identifier: Apache-2.0.

LogMetadata Schema:

This module defines the LogMetadata schema using Pydantic, which represents metadata and diagnostic information about
a log entry. It includes fields for processing notes, raw data, error logs, warnings, debug information, and processing time.

"""

from typing import Optional

from pydantic import BaseModel


class LogMetadata(BaseModel):
    """Represents metadata and diagnostic information about a log entry.

    Contains fields for processing notes, raw data, error logs, warnings, debug information, and processing time.

    Attributes:
        processing_notes (Optional[str]): Notes generated during log processing.
        raw_data (Optional[str]): Raw data associated with the log entry.
        error_logs (Optional[str]): Raw error logs from failed processing attempts.
        warnings (Optional[str]): Non-critical processing warnings.
        debug_info (Optional[str]): Supplementary debug info for development.
        processing_time (Optional[float]): Time taken to process the log entry, in seconds.
    """

    processing_notes: Optional[str]
    raw_data: Optional[str]
    error_logs: Optional[str]
    warnings: Optional[str]
    debug_info: Optional[str]
    processing_time: Optional[float]
