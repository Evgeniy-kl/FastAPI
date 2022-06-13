import json
import pika

credentials = pika.PlainCredentials('nzocntbp', 'bLDWuRiZsMh96jL2d0yCAiMvvWtBvpTr')
parameters = pika.ConnectionParameters('moose.rmq.cloudamqp.com',
                                       5672,
                                       'nzocntbp',
                                       credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare('fastapi_exchange')
channel.queue_declare(queue='fastapi_queue')
channel.queue_bind('fastapi_queue', 'fastapi_exchange', 'tests')


def publish(body):
    channel.basic_publish(
        body=json.dumps(body),
        exchange='fastapi_exchange',
        routing_key='tests',
    )


publish('HELLO FROM FASTAPI')
print('Message sent')
channel.close()
connection.close()
