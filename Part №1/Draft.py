from random import randint

def generate_unique_numbers(count, minbound, maxbound):
    if count > maxbound - minbound + 1:
        raise ValueError('Incorrect input parameters')
    ret = []
    while len(ret) < count:
        new = randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret


class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Cart:
    __rows = 3
    __nums_in_row = 5 
    __tab = ' '
    __delim = '--------------------------'
    __emptynum = 0
    __crossednum = -1

    def __init__(self):   
        uniques_count = self.__nums_in_row * self.__rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self.__card = []
        for _j in range(self.__rows):
            a = []
            for _i in range(self.__nums_in_row):
                num = randint(1, 91)
                if not num in a:
                    a.append('%+2s' % (num))
            a.sort()

            c = 0
            while c < 4:
                pos = randint(0, len(a) + c)
                a.insert(pos, '  ')
                c += 1

            string = ' '.join(a)
            self.__card.append(string)

    def __str__(self):  
        a = f'{self.__card[0]}\n{self.__card[1]}\n{self.__card[2]}\n{self.__delim}'
        return (a)         

    def __contains__(self, item):
        return item in self.__card

    def cross_num(self, num):
        for index, items in enumerate(self.__card):
            for item in enumerate(itmes)
            if item == num:
                self.__card[index] = self.__crossednum
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__card) == {self.__emptynum, self.__crossednum}

 
class Game:
    __usercard = None
    __compcard = None
    __numkegs = 90
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Cart()
        self.__compcard = Cart()
        self.__kegs = generate_unique_numbers(self.__numkegs, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
           useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break