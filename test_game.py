from game import *


def test_random_player_initialisation():
    rp = RandomPlayer()
    assert callable(rp.move)
