from unittest import TestCase

from main import Player, player_factory


class TestGame(TestCase):
    def test_create_player(self):
        player = player_factory()
        assert player.name == Player.DEFAULT_PLAYER_NAME