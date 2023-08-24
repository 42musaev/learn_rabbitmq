import pika


def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")


connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(username='root', password='1234')
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
queue_name = input('queue name: ')
channel.queue_declare(queue=queue_name)
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
