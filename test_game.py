from game import *


def test_random_player_initialisation():
    rp = RandomPlayer(Player)
    assert rp.self == "<__main__.Player object at 0x7fbdd8053340>"
