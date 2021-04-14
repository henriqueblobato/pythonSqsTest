import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='queue-test')

try:
    response = queue.send_message(
        MessageBody='<?xml version="1.0" encoding="UTF-8" ?><root><conta_origem><agencia>1</agencia><numero_conta>123456-7</numero_conta></conta_origem><conta_destino><agencia>1</agencia><numero_conta>765432-1</numero_conta></conta_destino><valor>1000</valor><moeda>BRL</moeda></root>')
    print('Mensagem envenenada enviada com sucesso!')
except:
    print('Ocorreu um erro ao enviar a mensagem')
