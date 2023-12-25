from game import *
import random
from unittest.mock import patch


def test_random_player_initialisation():
    rp = RandomPlayer()
    assert callable(rp.move)


def test_random_player_returns_paper():
    with patch('random.choice', return_value='paper'):
        rp = RandomPlayer()
        assert rp.move() == "paper"
