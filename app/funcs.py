from database.db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("PythhoDB")


def create_user(user: dict):
    try:
        response = table.put_item(Item=user)
        print(user)
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_user(email: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("user_email").eq(email)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_users():
    try:
        response = table.scan(
            AttributesToGet=["id", "user_email", 'qty_likes', 'qty_posts', 'qty_followers', 'created_at']
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_user(user: dict):
    try:
        response = table.delete_item(
            Key={
                "id": user["id"],
                "created_at": user["created_at"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
