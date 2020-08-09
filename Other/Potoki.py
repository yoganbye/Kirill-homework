# Реализовать решение следующей задачи: 
# «Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) 
# пишут в одну книгу. Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), 
# которые ждут не дождутся, чтобы прочитать новые записи из неё. Каждый читатель и писатель – 
# отдельный поток. Одновременно книгу может читать несколько читателей, но писать единовременно 
# может только один писатель.»


import threading
import random
import time

book = ''
mutex = threading.Lock()


def writing(timer, name):
    '''
    Функция в которой генерируется рандомный символ и последовательно
    с интервалом в 0.5 с добавляется в глобальную переменную book;
    потоки работают с методом Lock
    '''
    global book      
    mutex.acquire()
    for i in range(timer*2):        
        symbol = chr(random.randint(65,90)).lower()
        print(f'{name} пишет: {symbol}')
        book += symbol
        time.sleep(0.5)
    print(f'Книга содержит следующий текст:{book}')
    mutex.release()   


def reading(name, timer):
    '''
    функция прочтения
    '''
    while True:
        time.sleep(timer)
        print(f'{name} читает: {book}')


if __name__ == "__main__":
    def iter_writing(iter): 
        '''
        Количество итераций написания-прочтения текстов всеми лицами;
        '''
        for i in range(iter):
            time_of_writing_writer1 = 1
            time_of_writing_writer2 = 2

            flow_writer1 = threading.Thread(target=writing, args=(time_of_writing_writer1,
                                                                 'Писатель_1'))   
            flow_writer2 = threading.Thread(target=writing, args=(time_of_writing_writer2, 
                                                                'Писатель_2'))
            reader1 = threading.Thread(target = reading, args = ('Читатель1', 3))
            reader2 = threading.Thread(target = reading, args = ('Читатель2', 5))
            reader3 = threading.Thread(target = reading, args = ('Читатель3', 2))

            reader1.daemon = True
            reader2.daemon = True
            reader3.daemon = True
        
            flow_writer1.start()
            flow_writer2.start()
            reader1.start()
            reader2.start()
            reader3.start()
            
            flow_writer1.join()
            flow_writer2.join()
            reader1.join(0)
            reader2.join(0)
            reader2.join(0)


    iteration_wr = 2
    iter_writing(iteration_wr)
