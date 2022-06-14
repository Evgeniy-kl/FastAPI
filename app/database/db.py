from boto3 import resource
import os

dynamodb = resource('dynamodb',
                    endpoint_url=os.getenv('endpoint_url', 'http://dynamo-db-local:8000'),
                    aws_access_key_id=os.getenv('aws_access_key_id', 'dummy'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key', 'dummy'),
                    region_name=os.getenv('region_name', 'dummy'),
                    )

tables = [
    {
        "TableName": "PythonDB",
        "KeySchema": [
            {
                'AttributeName': 'user_email',
                'KeyType': 'HASH'
            }
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'user_email',
                'AttributeType': 'S'
            }
        ],
    },
]


def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)
