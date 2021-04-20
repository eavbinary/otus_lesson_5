from card import Card
from enum import Enum


class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2


class PlayerStatus(Enum):
    WIN = 1
    LOST = 2


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
        if self.__player_type == PlayerType.HUMAN:
            if not self.__card.strike_out(number):
                self.__status = PlayerStatus.LOST
                return
        else:
            self.__card.strike_out(number)

        if self.__card.get_win_status():
            self.__status = PlayerStatus.WIN
