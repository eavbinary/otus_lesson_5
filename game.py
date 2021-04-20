from random import randint
from player import Player, PlayerStatus, PlayerType


class Game:
    __count_kegs = 90
    __kegs = []
    __players = []

    @staticmethod
    def __generate_numbers(count, min, max):
        result = []
        if count > max - min + 1:
            raise ValueError('Не верные входные данные для генерации мешка с боченками.')
        while len(result) < count:
            number = randint(min, max)
            if number not in result:
                result.append(number)
        return result

    def start(self):
        self.__kegs = self.__generate_numbers(self.__count_kegs, 1, self.__count_kegs)

        for index, keg in enumerate(self.__kegs):
            print('\n\n')
            if self.__play_round(keg, self.__count_kegs - index - 1):
                return

    def add_player(self, type_player, name):
        self.__players.append(Player(type_player, name))

    def clear_players(self):
        self.__players.clear()

    def __play_round(self, keg, keg_left):
        print(f'Выпал бочонок: {keg} (осталось {keg_left})')
        for item in self.__players:
            if not item.status == PlayerStatus.LOST:
                item.show_card()

        for item in self.__players:
            if item.type == PlayerType.HUMAN:
                if not item.status == PlayerStatus.LOST:
                    choice = input(f'{item.name} зачеркнуть цифру? (y/n)')
                    if choice.lower() == 'y':
                        item.strike_out(keg)
            else:
                item.strike_out(keg)

        end_game = False
        for item in self.__players:
            if item.status == PlayerStatus.WIN:
                end_game = True
                print(f'{item.name} выиграл!!!')
        return end_game
