from match import *
import random
from unittest.mock import patch
import io


def test_random_player_initialisation():
    rp = RandomPlayer()
    assert callable(rp.move)


def test_random_player_returns_paper():
    with patch('random.choice', return_value='paper'):
        rp = RandomPlayer()
        assert rp.move() == "paper"


def test_play_round_beat_one():
    '''
    Test p1 = rock, p2 = scissors -> p1 wins
    '''
    with patch('match.beats', return_value=True), \
         patch.object(Player, 'move', side_effect=['rock', 'scissors']) as mock_move:
        
        game = Game(Player(), Player())

        # Redirect print statements to a StringIO for assertion
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.play_round()

        output = mock_stdout.getvalue().strip()

        # Add assertions based on your expected output
        assert "Player 1: rock  Player 2: scissors" in output
        assert "Player 1 WINS" in output


def test_play_round_beat_two():
    '''
    Test p1 = rock, p2 = scissors -> p1 wins
    '''
    with patch('match.beats', return_value=True), \
         patch.object(Player, 'move', side_effect=['scissors', 'paper']) as mock_move:
        
        game = Game(Player(), Player())

        # Redirect print statements to a StringIO for assertion
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.play_round()

        output = mock_stdout.getvalue().strip()

        # Add assertions based on your expected output
        assert "Player 1: scissors  Player 2: rock" in output
        assert "Player 1 WINS" in output
