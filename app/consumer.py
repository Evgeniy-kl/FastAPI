import pika
import models
from database.db import dynamodb
from services import DynamoManage
import json
from funcs import create_user


credentials = pika.PlainCredentials('nzocntbp', 'bLDWuRiZsMh96jL2d0yCAiMvvWtBvpTr')
parameters = pika.ConnectionParameters('moose.rmq.cloudamqp.com',
                                       5672,
                                       'nzocntbp',
                                       credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='django_queue')


def callback(ch, method, properties, body):
    table = dynamodb.Table("PythhoDB")
    print(f'Received: {body}')
    body = json.loads(body)
    user = models.UserStat(user_email=body['user'])
    if not table.get_item(
            Key={'user_email': user.user_email}
    ).get('Item'):
        print(create_user(user.dict()))
        print(user.dict())
    else:
        print('---')
    DynamoManage.increment_field(user.user_email, body['method'], table)


channel.basic_consume(queue='django_queue', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
