"""MongoDB handler for weather sensor and image metadata."""

import os
from datetime import datetime

from pymongo import MongoClient


class WeatherDB:
    """Handles MongoDB operations for sensor and image metadata."""

    def __init__(self, uri=None, db_name="weather_station"):
        """Initialize the WeatherDB client and define collections."""
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.client = MongoClient(self.uri)
        self.db = self.client[db_name]
        self.sensor_collection = self.db["sensor_data"]
        self.image_collection = self.db["cloud_images"]

    def insert_sensor_data(self, data: dict):
        """Insert a full weather sensor document (including image, validation, logs, etc.)."""
        # Ensure datetime parsing if timestamp is a string
        if isinstance(data.get("timestamp"), str):
            try:
                data["timestamp"] = datetime.fromisoformat(data["timestamp"])
            except ValueError:
                pass  # Let it be if it's already ISO-formatted correctly
        if isinstance(data.get("upload", {}).get("upload_time"), str):
            try:
                data["upload"]["upload_time"] = datetime.fromisoformat(
                    data["upload"]["upload_time"]
                )
            except (ValueError, KeyError, TypeError):
                pass
        self.sensor_collection.insert_one(data)

    def find_by_sensor_id(self, sensor_id: str):
        """Find a sensor document by its sensor_id."""
        return self.sensor_collection.find_one({"sensor_id": sensor_id})

    def insert_cloud_image_metadata(self, metadata: dict):
        """Insert metadata for a cloud image."""
        self.image_collection.insert_one(metadata)
