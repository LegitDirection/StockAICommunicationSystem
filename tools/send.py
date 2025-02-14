#!/usr/bin/env python
import pika 

class Send:
    def send_text(text, receiver):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue= receiver)
        channel.basic_publish(exchange='', routing_key='hello', body= text)
        print(" [x] Sent " + text)

    def send_stock_data(stock, bid, request, price, ):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue = receiver)
        channel.basic_publish(exchange=stock, routing_key='', body = stock +" "+ bid +" "+ request +" "+ price)

    def send_request(type, receiver):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue = receiver)
        channel.basic_publish(exchange='', routing_key='master', body = type +" "+ receiver)

    def send_new_subscriber(subscriber):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='subscriptions')
        channel.basic_publish(exchange='', routing_key='subscriptions', body = subscriber)
        print(" [x] Sent new subscriber " + subscriber)