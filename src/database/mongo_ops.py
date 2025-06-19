"""MongoDB ops for storing weather sensor data and cloud image metadata."""

from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.weather_station


def insert_sensor_data(cleaned_data: dict):
    """Insert cleaned sensor data into MongoDB collection.

    Args:
        cleaned_data (dict): Normalized data with ISO-formatted timestamp.
    """
    cleaned_data["timestamp"] = datetime.fromisoformat(cleaned_data["timestamp"])
    db.sensor_data.insert_one(cleaned_data)


def insert_cloud_image_metadata(metadata: dict):
    """Insert cloud image metadata into the database.

    Args:
        metadata (dict): Fields describing the uploaded image.
    """
    db.cloud_images.insert_one(metadata)
