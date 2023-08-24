import pika

connection_params = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(username='root', password='1234')
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
queue_name = input('queue name: ')
channel.queue_declare(queue=queue_name)
while True:
    message_body = input('message body: ')
    if message_body == '/stop':
        break
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message_body
    )

    print(f" [x] Sent '{message_body}'")
    connection.close()
