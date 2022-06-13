import decimal
from boto3.dynamodb.conditions import Key


class DynamoManage:
    @staticmethod
    def increment_field(email, field, table):
        print(f'SET #{field} = {field} + :val')
        table.update_item(
            TableName='PythhoDB',
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
