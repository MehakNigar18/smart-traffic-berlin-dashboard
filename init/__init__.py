# 01_Init

# Initialization: Define paths, set configurations, and import libraries
import pyspark # type: ignore
from pyspark.sql import SparkSession # pyright: ignore[reportMissingImports]

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Smart Mobility Project") \
    .getOrCreate()

# Set Blob Storage URL for the CSV data (configurable in your environment)
BLOB_STORAGE_URL = "https://mehaktrafficstore.blob.core.windows.net/traffic-data/"

# Check if Spark session is active
print(spark.version)
