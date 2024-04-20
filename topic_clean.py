from google.cloud import pubsub_v1

def clear_pubsub_messages(project_id, subscription_name):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    while True:
        response = subscriber.pull(
            subscription=subscription_path,
            max_messages=100
        )
        if not response.received_messages:
            break
        ack_ids = [message.ack_id for message in response.received_messages]
        subscriber.acknowledge(
            subscription=subscription_path,
            ack_ids=ack_ids
        )

    print("Pub/Sub messages cleared successfully.")

if __name__ == "__main__":
    project_id = "de-activity-420606"
    subscription_name = "my-sub"

    clear_pubsub_messages(project_id, subscription_name)
