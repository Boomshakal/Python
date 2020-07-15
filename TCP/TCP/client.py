import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

while True:
    data = input('>>>')

    if data == 'q':
        client.close()
        break

    client.send(data.encode('utf-8'))

    msg = client.recv(1024)
    print(msg.decode('utf-8'))