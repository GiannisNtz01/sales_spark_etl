from pyspark.sql.functions import col, sum as spark_sum

def transform(df):
    # Συνολικές πωλήσεις ανά κατηγορία
    sales_by_category = df.groupBy("PRODUCTLINE") \
                          .agg(spark_sum("SALES").alias("Total_Sales"))
    
    # Συνολικές πωλήσεις ανά περιοχή
    sales_by_region = df.groupBy("TERRITORY") \
                        .agg(spark_sum("SALES").alias("Total_Sales"))
    
    return df, sales_by_category, sales_by_region

if __name__ == "__main__":
    from extract import extract
    df = extract("data/sales_data.csv")
    transform(df)
