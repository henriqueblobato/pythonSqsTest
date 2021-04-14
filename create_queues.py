import boto3 as boto
import json

sqs = boto.resource('sqs')
sqs_client = boto.client('sqs')


# create a new queue
queue = sqs.create_queue(
    QueueName='queue-test',
    Attributes={
        'DelaySeconds': '5'
    }
)

dlq_queue = sqs.create_queue(QueueName='dlq-queue-test')

dlq_arn = dlq_queue.attributes.get('QueueArn')

redrive_policy = {
    'deadLetterTargetArn': dlq_arn,
    'maxReceiveCount': '3'
}

sqs_client.set_queue_attributes(
    QueueUrl=queue.url,
    Attributes={
        'RedrivePolicy': json.dumps(redrive_policy),
        'VisibilityTimeout': '5',
        'ReceiveMessageWaitTimeSeconds': 20
    }
)

sqs_client.set_queue_attributes(
    QueueUrl=dlq_queue.url,
    Attributes={
        'VisibilityTimeout': '5',
        'ReceiveMessageWaitTimeSeconds': 20
    }
)