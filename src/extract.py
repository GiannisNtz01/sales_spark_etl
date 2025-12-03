from pyspark.sql import SparkSession

def extract(file_path):
    spark = SparkSession.builder.appName("Sales ETL").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    df.show(5)
    return df

if __name__ == "__main__":
    extract("data/sales_data.csv")
