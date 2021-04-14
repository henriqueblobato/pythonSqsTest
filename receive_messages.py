import boto3
import json

sqs = boto3.resource('sqs')
sqs_client = boto3.client('sqs')

queue = sqs.get_queue_by_name(QueueName='queue-test')

messages = queue.receive_messages()

if(messages):
    for message in messages:
        try:
            message_body = json.loads(message.body)
            print('Processing message...')
            print(f'Transferring from account {message_body["origin_account"]["account_number"]} to account {message_body["destiny_account"]["account_number"]}')
            print(f'Transference value: {message_body["value"]}, currency {message_body["currency"]} completed!')
            sqs_client.delete_message(
                QueueUrl=queue.url,
                ReceiptHandle=message.receipt_handle
            )
            print('Message processed and deleted successfully!')
        except:
            print('Message ins not a JSON')
else:
    print('No message received')