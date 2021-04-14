import boto3
import json

sqs = boto3.resource('sqs')
sqs_client = boto3.client('sqs')

queue = sqs.get_queue_by_name(QueueName='dlq-queue-test')

messages = queue.receive_messages()

if(messages):
    for message in messages:
        print('Processing message from DLQ...')
        print(f'Message content: \n {message.body}')
        sqs_client.delete_message(
            QueueUrl=queue.url,
            ReceiptHandle=message.receipt_handle
        )
        print('DLQ message successfully processed and deleted!')
else:
    print('No message received from DLQ')