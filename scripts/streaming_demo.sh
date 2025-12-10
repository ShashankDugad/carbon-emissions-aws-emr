#!/bin/bash
echo "Starting consumer in background..."
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6 spark_streaming_consumer.py > consumer.log 2>&1 &
CONSUMER_PID=$!

echo "Waiting 15s for consumer initialization..."
sleep 15

echo "Sending 100 messages to Kafka..."
python3 kafka_producer.py

echo "Consumer running (will auto-stop at 60s). Waiting..."
wait $CONSUMER_PID

echo -e "\n=== RESULTS ==="
hdfs dfs -ls /user/hadoop/streaming_output
hdfs dfs -cat /user/hadoop/streaming_output/part-*.parquet 2>/dev/null | wc -c
