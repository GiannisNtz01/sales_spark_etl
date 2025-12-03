from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os


load_dotenv(dotenv_path="/Users/macbook/Desktop/sales_spark_etl/src/.env")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")


spark = SparkSession.builder \
    .appName("Sales Visualize") \
    .config("spark.jars", "/Users/macbook/Downloads/mysql-connector-j-9.5.0/mysql-connector-j-9.5.0.jar") \
    .getOrCreate()


url = f"jdbc:mysql://{MYSQL_HOST}:3306/{MYSQL_DB}"
properties = {
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "driver": "com.mysql.cj.jdbc.Driver"
}


df = spark.read.jdbc(url=url, table="sales_data", properties=properties)


pdf = df.toPandas()


plt.figure(figsize=(10,6))
sns.barplot(data=pdf, x="PRODUCTLINE", y="SALES", estimator=sum)
plt.title("Συνολικές Πωλήσεις ανά Product Line")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,6))
sns.barplot(data=pdf, x="COUNTRY", y="SALES", estimator=sum)
plt.title("Συνολικές Πωλήσεις ανά Χώρα")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))
sns.boxplot(data=pdf, x="DEALSIZE", y="SALES")
plt.title("Πωλήσεις ανά Deal Size")
plt.tight_layout()
plt.show()

spark.stop()
