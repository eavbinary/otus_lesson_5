from random import randint


class Card:
    __rows = 3
    __cols = 9
    __number_in_row = 5

    def __init__(self, header):
        self.__header = header
        numbers = sorted(self.__generate_numbers(self.__number_in_row * self.__rows, 1, 90))
        self.__data = []
        for row_index in range(0, self.__rows):
            self.__data.append(list())
            for index in range(0, self.__number_in_row):
                number_index = randint(0, len(numbers) - 1)
                self.__data[row_index].append(numbers[number_index])
                numbers.remove(numbers[number_index])

        for row_index in range(0, self.__rows):
            self.__data[row_index].sort()
            for index in range(0, self.__number_in_row):
                self.__data[row_index].insert(randint(0, self.__cols), ' ')

        self.__count_number = self.__number_in_row * self.__rows

    def __str__(self):
        result = f'Карточка {self.__header}\n'
        result += '-' * self.__cols * 3 + '\n'
        for row_index in range(0, self.__rows):
            for col_index in range(0, self.__cols):
                result += ' '
                if len(str(self.__data[row_index][col_index])) == 1:
                    result += ' '
                result += str(self.__data[row_index][col_index])
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
        for row_index in range(0, self.__rows):
            if number in self.__data[row_index]:
                for col_index in range(0, self.__cols):
                    if self.__data[row_index][col_index] ==  number:
                        self.__data[row_index][col_index] = '-'
                        self.__count_number -= 1
                        return True
        return False

    def get_win_status(self):
        return not self.__count_number > 0

