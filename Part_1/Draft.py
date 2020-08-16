def get_message(sock, name):
    while True:
        message = input('[You]: ')
        timest = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())

        born_json = json_convert(name,message, timest)

        if message != "":
            sock.sendto((born_json).encode('utf-8'), server)