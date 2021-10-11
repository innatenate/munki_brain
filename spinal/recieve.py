import socket
import json
from stem import callosum
host = "192.168.1.8"
port = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(3)

while True:
    client, clientAddr = server.accept()
    print(f"Munki attempt connect {clientAddr[0]}")
    message = client.recv(2450)
    message = message.decode('utf-8')
    message = json.loads(message)
    if message['request'] == 'command':
        print(message['command'])
        success, phrase = callosum.process_request({'type':'commandfire', 'msg':message['command']}, 'clientrequest', message['profile'])
        if success:
            client.send(phrase.encode('utf-8'))
        else:
            phrase = json.dumps({'type': 'error', 'phrase': "There was a problem running the command. I apologize. Please try again."})
            client.send(phrase.encode('utf-8'))
    elif message['request'] == 'query':
        print(message['command'])
        success, phrase = callosum.process_request({'type':'query', 'msg':message['command']}, 'clientrequest', message['profile'])
        if success:
            client.send(phrase.encode('utf-8'))
        else:
            phrase = json.dumps({'type': 'error', 'phrase': "There was a problem running the query. I apologize. Please try running the query again."})
            client.send(phrase.encode('utf-8'))