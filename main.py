from game import Game
from player import PlayerType

if __name__ == '__main__':
    game = Game()
    while True:
        player_count = int(input(f'Количество игроков:'))
        computer_index = 1
        for player in range(0, player_count):
            player_type_human = input(f'Игрок номер {player + 1} человек? (y/n)')
            if player_type_human.lower() == 'y':
                player_type_in = PlayerType.HUMAN
                player_name_in = input(f'Введите имя игрока номер {player + 1}:')
            else:
                player_type_in = PlayerType.COMPUTER
                player_name_in = f"Компьютер {computer_index}"
                computer_index += 1
            game.add_player(player_type_in, player_name_in)

        game.start()

        new_game = input(f'Новая игра? (y/n)')
        if not new_game.lower() == 'y':
            break
        game.clear_players()
