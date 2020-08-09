import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создать сокет TCP
client_socket.connect(('localhost', 8888))  # Соединиться с сервером
data = client_socket.recv(1024)  # Принять не более 1024 байтов данных
client_socket.close()
print("Текущее время: %s" % data.decode('ascii'))

