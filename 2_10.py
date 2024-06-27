import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, skill):
        threading.Thread.__init__(self)  # super().__init__() не работает! Поэтому я обратился на прямую к Thread
        self.name = name
        self.skill = skill
        self.enemies = 100

    def run(self):
        print(f'{self.name}, враги у ворот')
        day = 0
        print('----------------------------------------------')
        while self.enemies > 0:
            day += 1
            time.sleep(1)
            self.enemies -= self.skill
            print(f'{self.name}, сражается {day} день(дня), врагов осталось {self.enemies} воинов.')
            print('-----------------------------------------------')
        print(f'{self.name} одержал победу спустя {day} дней!')
        print('----------------------------------------------')


knight1 = Knight('Сер Новичёк', 10)
knight2 = Knight('Сер Киберспортсмен', 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Все битвы закончились!')
