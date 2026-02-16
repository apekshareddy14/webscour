import pika

# Seed URLs
seed_urls = [
    "https://example.com",
    "https://httpbin.org"
]

# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='url_queue')

# Publish seed URLs
for url in seed_urls:
    channel.basic_publish(
        exchange='',
        routing_key='url_queue',
        body=url
    )
    print(f"Sent: {url}")

connection.close()
print("Producer finished.")
