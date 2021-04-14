import boto3
import json

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='queue-test')

try:
    response = queue.send_message(
        MessageBody=json.dumps({
            'origin_account': {
                'agency': '0001',
                'account_number': '123456-7',
            },
            'destiny_account': {
                'agency': '0001',
                'account_number': '765432-1'
            },
            'value': 1000,
            'currency': 'BRL'
        })
    )
    print('Transference done')
except:
    print('An error has occurred')
