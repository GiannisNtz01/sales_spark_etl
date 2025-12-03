from pyspark.sql import SparkSession
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="/Users/macbook/Desktop/sales_spark_etl/src/.env")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

spark = SparkSession.builder \
    .appName("Sales ETL") \
    .config("spark.jars", "/Users/macbook/Downloads/mysql-connector-j-9.5.0/mysql-connector-j-9.5.0.jar") \
    .getOrCreate()

df = spark.read.csv("data/sales_data.csv", header=True, inferSchema=True)

# JDBC connection properties
url = f"jdbc:mysql://{MYSQL_HOST}:3306/{MYSQL_DB}"
properties = {
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "driver": "com.mysql.cj.jdbc.Driver"
}

df.write.jdbc(url=url, table="sales_data", mode="overwrite", properties=properties)

spark.stop()
