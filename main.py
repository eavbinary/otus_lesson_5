from random import randint


class Card:
    __rows = 3
    __cols = 9
    __number_in_row = 5

    def __init__(self, header):
        self.__header = header
        numbers = sorted(self.__generate_numbers(self.__number_in_row * self.__rows, 1, 90))
        self.__data = []
        for r in range(0, self.__rows):
            self.__data.append(list())
            for i in range(0, self.__number_in_row):
                number_index = randint(0, len(numbers) - 1)
                self.__data[r].append(numbers[number_index])
                numbers.remove(numbers[number_index])

        for r in range(0,self.__rows):
            self.__data[r].sort()
            for i in range(0, self.__number_in_row):
                self.__data[r].insert(randint(0, self.__cols), ' ')

        self.__count_number = self.__number_in_row * self.__rows

    def __str__(self):
        result = 'Карточка ' + self.__header + '\n'
        result += '-' * self.__cols * 3 + '\n'
        for r in range(0, self.__rows):
            for c in range(0, self.__cols):
                result += ' '
                if len(str(self.__data[r][c])) == 1:
                    result += ' '
                result += str(self.__data[r][c])
            result += '\n'
        result += '-' * self.__cols * 3
        return result

    @staticmethod
    def __generate_numbers(count, min, max):
        result = []
        if count > max - min + 1:
            raise ValueError('Не верные входные данные для генерации карточки.')
        while len(result) < count:
            number = randint(min, max)
            if number not in result:
                result.append(number)
        return result

    def strike_out(self, number):
        for r in range(0, self.__rows):
            if number in self.__data[r]:
                for c in range(0, self.__cols):
                    if self.__data[r][c] ==  number:
                        self.__data[r][c] = '-'
                        self.__count_number -= 1
                        return True
        return False

    def get_win_status(self):
        return False if self.__count_number > 0 else True


class Player:
    def __init__(self, player_type, player_name):
        self.__player_name = player_name
        self.__player_type = player_type
        self.__card = Card(player_name)
        self.__status = None

    @property
    def type(self):
        return self.__player_type

    @property
    def name(self):
        return self.__player_name

    @property
    def status(self):
        return self.__status

    def show_card(self):
        print(self.__card)

    def strike_out(self, number):
        if self.__player_type == 'Human':
            if not self.__card.strike_out(number):
                self.__status = 'lost'
                return
        else:
            self.__card.strike_out(number)

        if self.__card.get_win_status():
            self.__status = 'win'


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

    def add_player(self, type_payer, name):
        self.__players.append(Player(type_payer, name))

    def clear_players(self):
        self.__players.clear()

    def __play_round(self, keg, keg_left):
        print(f'Выпал бочонок: {keg} (осталось {keg_left})')
        for item in self.__players:
            if not item.status == 'lost':
                item.show_card()

        for item in self.__players:
            if item.type == "Human":
                if not item.status == 'lost':
                    choice = input(f'{item.name} зачеркнуть цифру? (y/n)')
                    if choice.lower() == 'y':
                        item.strike_out(keg)
            else:
                item.strike_out(keg)

        end_game = False
        for item in self.__players:
            if item.status == 'win':
                end_game = True
                print(f'{item.name} выиграл!!!')
        return end_game


if __name__ == '__main__':
    game = Game()
    while True:
        player_count = int(input(f'Количество игроков:'))
        computer_index = 1
        for player in range(0, player_count):
            player_type_human = input(f'Игрок номер {player + 1} человек? (y/n)')
            if player_type_human.lower() == 'y':
                player_type_in = 'Human'
                player_name_in = input(f'Введите имя игрока номер {player + 1}:')
            else:
                player_type_in = 'Computer'
                player_name_in = f"Компьютер {computer_index}"
                computer_index += 1
            game.add_player(player_type_in, player_name_in)

        game.start()

        new_game = input(f'Новая игра? (y/n)')
        if not new_game.lower() == 'y':
            break
        game.clear_players()
