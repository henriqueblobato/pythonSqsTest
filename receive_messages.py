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
            print('Processando mensagem...')
            print(f'Realizando trasnferência da conta {message_body["conta_origem"]["numero_conta"]} para a conta {message_body["conta_destino"]["numero_conta"]}')
            print(f'Transferência no valor de {message_body["valor"]} {message_body["moeda"]} efetivada!')
            sqs_client.delete_message(
                QueueUrl=queue.url,
                ReceiptHandle=message.receipt_handle
            )
            print('Mensagem processada (e excluída) com sucesso!')
        except:
            print('Mensagem não está no formato JSON')
else:
    print('Nenhuma mensagem recebida')