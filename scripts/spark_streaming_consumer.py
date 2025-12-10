from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder \
    .appName("Kafka_Streaming_Consumer") \
    .getOrCreate()

schema = StructType() \
    .add("timestamp", StringType()) \
    .add("state", StringType()) \
    .add("pollutant", StringType()) \
    .add("value", DoubleType()) \
    .add("unit", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "air_quality") \
    .option("startingOffsets", "earliest") \
    .load()

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = parsed.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "hdfs://ip-172-31-12-52.ap-south-1.compute.internal:8020/user/hadoop/streaming_output") \
    .option("checkpointLocation", "hdfs://ip-172-31-12-52.ap-south-1.compute.internal:8020/user/hadoop/streaming_checkpoint") \
    .start()

query.awaitTermination(60)
spark.stop()
