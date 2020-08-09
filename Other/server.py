import socket


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #протоколы сокета
    server_socket.bind(('localhost', 5000)) #связь этого субьекта с конкретным адресом и портом
    server_socket.listen() #даем указание на прослушивание адреса и порта

    while True: #т.к. не знаем на сколько длинная сессия
        client_socket, addr = server_socket.accept()#просмотр данных от клиента; accept возвращает кортеж
                                                    #распаковываем сокет(0) и адрес(1)
        request = client_socket.recv(1024)#то что прислал клиент и ограничение по байтам
        print(request.decode('utf-8'))
        print()
        print(addr)

        client_socket.sendall('Hello boy'.encode())#отвечаем клиентскому сокету; encode - в байты
        client_socket.close()#закрываем соединение, т.к. иначе ничего не увидим
     


if __name__ == "__main__":
    run()
