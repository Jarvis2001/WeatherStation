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

    def insert_sensor_data(self, cleaned_data: dict):
        """Insert cleaned sensor data with ISO timestamp."""
        cleaned_data["timestamp"] = datetime.fromisoformat(cleaned_data["timestamp"])
        self.sensor_collection.insert_one(cleaned_data)

    def insert_cloud_image_metadata(self, metadata: dict):
        """Insert metadata for a cloud image."""
        self.image_collection.insert_one(metadata)
