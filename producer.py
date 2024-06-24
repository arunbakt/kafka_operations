from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:29092, localhost:39092, localhost:49092')
for i in range(5000):
    producer.send('test-topic', key=bytes(str(i), 'utf-8'), value=bytes('message-' + str(i), 'utf-8'))
    time.sleep(1)
producer.close()
