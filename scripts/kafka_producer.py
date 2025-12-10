from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

states = ['California', 'Texas', 'New York', 'Florida']
pollutants = ['PM2.5', 'CO', 'NO2', 'SO2', 'O3']

print("Sending air quality data to Kafka...")
for i in range(100):
    data = {
        'timestamp': datetime.now().isoformat(),
        'state': random.choice(states),
        'pollutant': random.choice(pollutants),
        'value': round(random.uniform(5, 50), 2),
        'unit': 'ug/m3'
    }
    producer.send('air_quality', value=data)
    print(f"Sent: {data}")
    time.sleep(0.5)

producer.close()
print("Done sending 100 records")
