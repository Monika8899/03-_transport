from google.cloud import pubsub_v1
import json

project_id = "de-activity-420606"
topic_name = "my-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

file_path = r"C:\Users\KAMINENI MONIKA\Desktop\bcsample (2).json"

with open(file_path, "r") as file:
    data = json.load(file)

for index, record in enumerate(data[:1000]):

    record_bytes = json.dumps(record).encode("utf-8")
    future = publisher.publish(topic_path, data=record_bytes)
    print(f"Published message {index + 1}: {future.result()}")

print("All messages published.")
