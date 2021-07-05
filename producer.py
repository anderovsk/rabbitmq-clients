#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('devops', 'devops')
parameters = pika.ConnectionParameters('$(rabbitmq-host)',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='hello')
print(" [x] Sent 'Hello World!'")
connection.close()