# AWS - SQS with Lambda

### Send message
>  [Function url](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/sendMessageSQS?newFunction=true&tab=code)


Config a message on test and send. A simple string will go to Dead Letter Queue, a string from a json will be processed and deleted by the next function.

Example:

Accepted string on queue: `"{\"value\": \"Hello World\"}"`

This message will go to DLQ: `"Hello World"`



[Check logs here](https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252FsendMessageSQS)

### Check SQS message
> [Function url](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/checkSQSMessage?tab=code)

This function is called when the queue receives a new message. Will check if the message is a json, if it is, the message is printed and deleted, if not it raises an error and the message stays in the queue until going to DLQ.

[Check logs here](https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252FcheckSQSMessage)