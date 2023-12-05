from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration for InfluxDB connection
INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")

class DatabaseManager:
    def __init__(self):
        self.client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_pressure_reading(self, reading, timestamp):
        """
        Write a new pressure reading to the database.
        :param reading: The pressure reading value.
        :param timestamp: The timestamp of the reading.
        """
        point = Point("pressure").tag("unit", "psi").field("value", reading).time(timestamp)
        self.write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

    def query_pressure_readings(self, start: str, stop: str):
        """
        Query pressure readings from the database within a time range.
        :param start: The start time for the query.
        :param stop: The stop time for the query.
        :return: List of pressure readings.
        """
        query = f'from(bucket: "{INFLUXDB_BUCKET}") |> range(start: {start}, stop: {stop}) |> filter(fn: (r) => r._measurement == "pressure")'
        tables = self.client.query_api().query(query, org=INFLUXDB_ORG)
        results = []
        for table in tables:
            for record in table.records:
                results.append((record.get_time(), record.get_value()))
        return results

    def close(self):
        self.client.close()

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager()
    
    # Example write
    db_manager.write_pressure_reading(30.5, "2023-04-01T00:00:00Z")
    
    # Example query
    readings = db_manager.query_pressure_readings("2023-04-01T00:00:00Z", "2023-04-02T00:00:00Z")
    for time, value in readings:
        print(f"Time: {time}, Value: {value}")
    
    db_manager.close()
