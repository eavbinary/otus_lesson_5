import pytest
from player import Player, PlayerStatus, PlayerType


class TestPlayer:
    @pytest.mark.parametrize("player_type",[
        PlayerType.HUMAN,
        PlayerType.COMPUTER,
    ])
    def test_player_type(self, player_type):
        player = Player(player_type, "TestPlayer")
        assert player.type == player_type

    def test_player_name(self):
        player_name = "TestPlayer"
        player = Player(PlayerType.HUMAN, player_name)
        assert player.name == player_name

    def test_player_status_input_wrong_keg(self):
        player = Player(PlayerType.HUMAN, "TestPlayer")
        player.strike_out(100)
        assert player.status == PlayerStatus.LOST


