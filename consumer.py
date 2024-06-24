import random

from kafka import KafkaConsumer

random_id = random.randint(0, 1000)
# Initialize the Kafka consumer
consumer = KafkaConsumer(
    'test-topic',                             # Topic to subscribe to
    bootstrap_servers=['localhost:29092', 'localhost:39092', 'localhost:49092'],    # Kafka broker(s)
    auto_offset_reset='earliest',             # Where to start reading from if no offset is present
    enable_auto_commit=True,                  # Auto-commit the offsets
    group_id=f'my-group-{random_id}',                      # Consumer group ID
    key_deserializer=lambda x: x.decode('utf-8'),  # Deserializer for the message key
    value_deserializer=lambda x: x.decode('utf-8') # Deserializer for the message value
)

print("Started consuming messages...")

# Consume messages from the topic
for message in consumer:
    print(f"Received message: key={message.key}, value={message.value}")

print("Stopped consuming messages.")
