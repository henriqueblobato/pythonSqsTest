# SQS 

### Step 1

Create an IAM user
* Don't forget to add `AmazonSQSFullAccess` permission

### Step 2
Configure aws credentials locally
> aws configure

### Step 3
Create a virtualenv
> python -m venv <YOUR_VIRTUALENV>

> source <YOUR_VIRTUALENV>/bin/activate

### Step 4
Install requirements

> pip install -r requirements.txt

### Step 5
Run
> python `create_queues.py`

Then check your AWS console (be sure about the  region), there will be two new queues: `queue-test` and `dlq-queue-test`

Now you can run any other file! 

## Files:

### `send_message.py`
Will send a string of a json as a message to `queue-test`.

### `receive_message.py`
Will receive all messages trying to transform them to a json using json.loads() and delete all read. If can't transform the message, will print an error message.

* Note: to a message fail 3 times on being read, it will be directed to `dlq-queue-test`

### `send_poison_message.py`
Will send an XML message to fail on `receive_message.py`.

### `receive_dlq_messages.py`
Will receive all messages from DLQ, print them, and delete them.

