from database.db import dynamodb
import pika
from boto3.dynamodb.conditions import Key


class DynamoManage:
    @staticmethod
    def increment_field(email, field, table):
        print(f'SET #{field} = {field} + :val')
        table.update_item(
            TableName='PythonDB',
            Key={
                'user_email': email
            },
            UpdateExpression='SET #s = #s + :val',
            ExpressionAttributeNames={
                "#s": f'{field}'
            },
            ExpressionAttributeValues={
                ':val': 1
            },
            ReturnValues="UPDATED_NEW"

        )


class RabbitManage:

    def __init__(self, host, port: int, virtualhost, username, password):
        self.host = host
        self.port = port
        self.virtualhost = virtualhost
        self.username = username
        self.password = password

    def connect(self, queue):
        creds = pika.PlainCredentials(self.username, self.password)
        params = pika.ConnectionParameters(self.host,
                                           self.port,
                                           self.virtualhost,
                                           creds)

        connection = pika.BlockingConnection(params)

        channel = connection.channel()

        try:
            channel.queue_declare(queue=queue)
            print(f'Connected to {queue}')
        except ConnectionError as e:
            print(e)

        return channel


class UserManage:
    table = dynamodb.Table("PythonDB")

    @staticmethod
    def get_user(email: str):
        response = UserManage.table.query(
            KeyConditionExpression=Key("user_email").eq(email)
        )
        return response["Items"]

    @staticmethod
    def get_users():
        response = UserManage.table.scan(
            AttributesToGet=["id", "user_email", 'qty_likes', 'qty_posts', 'qty_followers', 'created_at']
        )
        return response["Items"]

    @staticmethod
    def delete_user(email: str):
        response = UserManage.table.delete_item(
            Key={
                "user_email": email
            }
        )
        return response
