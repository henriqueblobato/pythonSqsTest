import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='queue-test')

try:
    response = queue.send_message(
        MessageBody='<?xml version="1.0" encoding="UTF-8" ?><root><origin_account><agency>1</agency><number_account>123456-7</number_account></origin_account><destiny_account><agency>1</agency><number_account>765432-1</number_account></destiny_account><value>1000</value><currency>BRL</currency></root>')
    print('Poison message sent successfully!')
except:
    print('An error has occurred to sent poison message')
