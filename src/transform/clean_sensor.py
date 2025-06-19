"""
data_cleaner.py

This module provides functionality to clean and transform raw sensor data 
from an IoT-based weather station into a standardized and enriched format 
for storage and downstream machine learning processing.

Core Features:
- Converts temperature from Celsius to Kelvin
- Converts wind speed from m/s to km/h
- Converts pressure from hPa to Pascals
- Parses boolean values from strings
- Normalizes numeric values and strips whitespace
- Supports extensible schema for diverse weather sensor types

Usage:
    from data_cleaner import clean_sensor_data

    raw = {
        "temperature_c": "25.0",
        "humidity": "80",
        "sensor_id": "WX-001"
    }
    cleaned = clean_sensor_data(raw)
"""

import logging
logging.basicConfig(level=logging.INFO)
from typing import Callable

def c_to_k(c): return float(c) + 273.15
def mps_to_kph(mps): return float(mps) * 3.6
def hpa_to_pa(hpa): return float(hpa) * 100
def parse_bool(val): return str(val).strip().lower() in ["true", "yes", "1", "good", "valid"]
def identity(x): return str(x).strip() if x else None
def as_float(x): return float(x) if x not in [None, ""] else None

# Mapping: raw field -> (clean field, transformation function)
FIELD_MAP: dict[str, tuple[str, Callable]] = {
    "temperature_c": ("temperature_k", c_to_k),
    "dew_point_c": ("dew_point_k", c_to_k),
    "heat_index_c": ("heat_index_k", c_to_k),
    "wind_speed_mps": ("wind_speed_kph", mps_to_kph),
    "pressure_hpa": ("pressure_pa", hpa_to_pa),
    "humidity": ("humidity", as_float),
    "wind_direction": ("wind_direction", as_float),
    "battery_level": ("battery_level", as_float),
    "signal_strength": ("signal_strength", as_float),
    "data_quality": ("data_quality", parse_bool),
    "anomaly_detected": ("anomaly_detected", parse_bool),
    # Fields with only trimming
    "sensor_id": ("sensor_id", identity),
    "timestamp": ("timestamp", identity),
    "location": ("location", identity),
    "comments": ("comments", identity),
    "sensor_type": ("sensor_type", identity),
    "manufacturer": ("manufacturer", identity),
    "model": ("model", identity),
    "firmware_version": ("firmware_version", identity),
    "calibration_data": ("calibration_data", identity),
    "raw_data": ("raw_data", identity),
    "data_source": ("data_source", identity),
    "upload_time": ("upload_time", identity),
    "upload_status": ("upload_status", identity),
    "processing_notes": ("processing_notes", identity),
    "quality_flags": ("quality_flags", identity),
    "anomaly_type": ("anomaly_type", identity),
    "anomaly_severity": ("anomaly_severity", identity),
    "anomaly_timestamp": ("anomaly_timestamp", identity),
    "anomaly_resolution": ("anomaly_resolution", identity),
    "anomaly_comments": ("anomaly_comments", identity),
    "sensor_status": ("sensor_status", identity),
    "sensor_location": ("sensor_location", identity),
    "sensor_calibration": ("sensor_calibration", identity),
    "sensor_accuracy": ("sensor_accuracy", identity),
    "sensor_precision": ("sensor_precision", identity),
}

def clean_sensor_data(sensor_data: dict) -> dict:
    """
    Cleans and transforms raw sensor input data.

    Args:
        sensor_data (dict): Raw data dictionary from a weather sensor or API.
    
    Returns:
        dict: A dictionary with cleaned and normalized fields, ready for storage or ML processing.
    
    Notes:
        - Fields not present in the input will be skipped.
        - If a transformation fails, the field will be set to None.
    """
    logging.info("Cleaning sensor data: %s at %s", 
                 sensor_data.get("sensor_id", "unknown"),
                 sensor_data.get("timestamp", "unknown"))
    
    cleaned = {}
    for raw_field, (clean_field, transformer) in FIELD_MAP.items():
        if raw_field in sensor_data:
            try:
                cleaned[clean_field] = transformer(sensor_data[raw_field])
            except Exception:
                cleaned[clean_field] = None
    return cleaned
