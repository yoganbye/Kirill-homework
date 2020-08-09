import threading

import time


def run():
    i = 1

    # Бесконечный цикл
    while True:
        print(i)
        i += 1

        time.sleep(0.5)


if __name__ == '__main__':
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    thread.join(4)

    print('Quit!')