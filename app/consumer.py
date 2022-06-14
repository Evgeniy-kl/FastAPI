import schema
from database.db import dynamodb
from services import DynamoManage
import json
from services import UserManage
from services import RabbitManage
import os

connection_obj = RabbitManage(
    os.getenv('host', 'moose.rmq.cloudamqp.com'),
    os.getenv('port', 5672),
    os.getenv('virtualhost', 'nzocntbp'),
    os.getenv('username', 'nzocntbp'),
    os.getenv('password', 'bLDWuRiZsMh96jL2d0yCAiMvvWtBvpTr')
)
channel = connection_obj.connect('django_queue')


def callback(body):
    table = dynamodb.Table("PythonDB")
    print(f'Received: {body}')
    body = json.loads(body)
    user = schema.UserStat(user_email=body['user'])
    if not table.get_item(
            Key={'user_email': user.user_email}
    ).get('Item'):
        UserManage.create_user(user.dict())
    else:
        print('EXISTING ROW')
    DynamoManage.increment_field(user.user_email, body['method'], table)


channel.basic_consume(queue='django_queue', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
