import os
import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):

  text_message = "Congrats! You deployed this application using a CI/CD pipeline."

  phone_number = os.environ['MY_PHONE_NUMBER']

  publish_sns_update(text_message)

  # add error handling, phone number last four digits

def publish_sns_update(text_message):

  response = sns_client.publish(
      TargetArn = os.environ['SNS_TOPIC_ARN'], 
      Message=json.dumps({'default': text_message}),
      MessageStructure='json'
  )

  return response