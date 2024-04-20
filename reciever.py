from google.cloud import pubsub_v1

def receive_messages(project_id, subscription_name):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message):
        print(f"Received message: {message.data}")
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    print(f"Listening for messages on {subscription_path}...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopped receiving messages.")

if __name__ == "__main__":
    project_id = "de-activity-420606"
    subscription_name = "my-sub"

    receive_messages(project_id, subscription_name)