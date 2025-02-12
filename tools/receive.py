import pika


def receive_text(sender):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=sender)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        return body
    channel.basic_consume(queue=sender, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return callback


def receive_stock_data(stock):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=stock)
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        return body
    channel.basic_consume(queue=stock, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return callback


def receive_request():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='master_request')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        return body
    channel.basic_consume(queue='master_request', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return callback