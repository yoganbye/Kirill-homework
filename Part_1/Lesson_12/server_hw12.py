import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создает сокет TCP
server_socket.bind(('', 8888))  # Присваивает порт 8888
server_socket.listen(1)  # Переходит в режим ожидания запросов;
# одновременно обслуживает не более
# 5 запросов.

while True:
   client_socket, addr = server_socket.accept()  # Принять запрос на соединение
   print("Получен запрос на соединение от %s" % str(addr))
   timestr = time.ctime(time.time()) + "\n"
   client_socket.send(timestr.encode('ascii'))
   client_socket.close()


