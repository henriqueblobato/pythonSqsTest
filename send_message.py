import boto3
import json

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='queue-test')

try:
    response = queue.send_message(
        MessageBody=json.dumps({
            'conta_origem': {
                'agencia': '0001',
                'numero_conta': '123456-7',
            },
            'conta_destino': {
                'agencia': '0001',
                'numero_conta': '765432-1'
            },
            'valor': 1000,
            'moeda': 'BRL'
        })
    )
    print('Transação realizada')
except:
    print('Ocorreu um erro ao realizar a transação')
