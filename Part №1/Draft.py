# «Пять безмолвных философов сидят вокруг круглого стола, перед каждым философом стоит 
# тарелка спагетти. Вилки лежат на столе между каждой парой ближайших философов. 
# Каждый философ может либо есть, либо размышлять. Прием пищи не ограничен количеством 
# оставшихся спагетти — подразумевается бесконечный запас. Тем не менее, философ может 
# есть только тогда, когда держит две вилки — взятую справа и слева (альтернативная 
# формулировка проблемы подразумевает миски с рисом и палочки для еды вместо тарелок 
# со спагетти и вилок). Каждый философ может взять ближайшую вилку (если она доступна) 
# или положить — если он уже держит её. Взятие каждой вилки и возвращение её на стол 
# являются раздельными действиями, которые должны выполняться одно за другим. Вопрос 
# задачи заключается в том, чтобы разработать модель поведения (параллельный алгоритм), 
# при котором ни один из философов не будет голодать, то есть будет вечно чередовать 
# приём пищи и размышления.»
import threading
import time


class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False

# The philosopher thread
def philosopher(left, right):
    while True:
        with acquire(left,right):      
            time.sleep(0.5)  
            print(f'Philosopher at {threading.currentThread()} is eating.')

# The chopsticks
N_FORKS = 5
forks = [threading.Lock() for n in range(N_FORKS)]

# Create all of the philosophers
phils = [threading.Thread(
    target=philosopher,
    args=(forks[n], forks[(n + 1) % N_FORKS])
) for n in range(N_FORKS)]

# Run all of the philosophers
for p in phils:
    p.start()