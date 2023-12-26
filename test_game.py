from match import *
import random
from unittest.mock import patch
import io
import unittest


def test_random_player_initialisation():
    rp = RandomPlayer()
    assert callable(rp.move)


def test_random_player_returns_paper():
    with patch('random.choice', return_value='paper'):
        rp = RandomPlayer()
        assert rp.move() == "paper"


def test_play_round_beat_one():
    
    '''Test p1 = rock, p2 = scissors -> p1 wins'''
    with patch('match.beats', return_value=True), \
         patch.object(Player, 'move', side_effect=['rock', 'scissors']) as mock_move:
        
        game = Game(Player(), Player())

        # Redirect print statements to a StringIO for assertion
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.play_round()

        output = mock_stdout.getvalue().strip()

        # Add assertions based on your expected output
        assert "Player 1: rock Player 2: scissors" in output
        assert "Player 1 wins" in output


def test_play_round_beat_two():
    '''Test p1 = scissors, p2 = rock -> p1 wins'''
    with patch('match.beats', return_value=True), \
         patch.object(Player, 'move', side_effect=['scissors', 'paper']) as mock_move:
        
        game = Game(Player(), Player())

        # Redirect print statements to a StringIO for assertion
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.play_round()

        output = mock_stdout.getvalue().strip()

        # Add assertions based on your expected output
        assert "Player 1: scissors Player 2: paper" in output
        assert "Player 1 wins" in output


def test_play_round_beat_three():
    '''Test p1 = paper, p2 = rock -> p1 wins'''
    with patch('match.beats', return_value=True), \
         patch.object(Player, 'move', side_effect=['paper', 'rock']) as mock_move:
        
        game = Game(Player(), Player())

        # Redirect print statements to a StringIO for assertion
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.play_round()

        output = mock_stdout.getvalue().strip()

        # Add assertions based on your expected output
        assert "Player 1: paper Player 2: rock" in output
        assert "Player 1 wins" in output


def test_p2_beats_p1_scissors_v_rock(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['scissors', 'rock']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: scissors Player 2: rock" in captured.out
        assert "Player 2 wins\n" in captured.out


def test_p2_beats_p1_paper_v_scissors(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['paper', 'scissors']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: paper Player 2: scissors" in captured.out
        assert "Player 2 wins\n" in captured.out


def test_p2_beats_p1_rock_v_paper(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['rock', 'paper']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: rock Player 2: paper" in captured.out
        assert "Player 2 wins\n" in captured.out


def test_match_rock_v_rock(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['rock', 'rock']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: rock Player 2: rock" in captured.out
        assert "It is a tie\n" in captured.out


def test_match_paper_v_paper(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['paper', 'paper']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: paper Player 2: paper" in captured.out
        assert "It is a tie\n" in captured.out


def test_match_paper_v_paper(capsys):
    with patch('match.beats', return_value=False), \
         patch.object(Player, 'move', side_effect=['scissors', 'scissors']):

        game = Game(Player(), Player())

        # Call play_round
        game.play_round()

        # Capture the printed output
        captured = capsys.readouterr()

        # Print the captured output to the terminal
        print("Captured Output:")
        print(captured.out)

        # Access captured stdout and check its content
        assert "Player 1: scissors Player 2: scissors" in captured.out
        assert "It is a tie\n" in captured.out


def test_huamn_player_initialisation():
    hp = HumanPlayer()
    assert callable(hp.move)


class TestHumanPlayer(unittest.TestCase):
    @patch('builtins.input', return_value='r')
    def test_move_returns_rock(self, mock_input):
        human_player = HumanPlayer()
        self.assertEqual(human_player.move(), 'r')

    @patch('builtins.input', return_value='p')
    def test_move_returns_paper(self, mock_input):
        human_player = HumanPlayer()
        self.assertEqual(human_player.move(), 'p')

    @patch('builtins.input', return_value='s')
    def test_move_returns_scissors(self, mock_input):
        human_player = HumanPlayer()
        self.assertEqual(human_player.move(), 's')


class TestReflectPlayer(unittest.TestCase):
    def test_prev_round(self):
        reflect_player = ReflectPlayer()

        with patch('match.Player.learn') as mock_learn:
            reflect_player.prev_round('rock', 'scissors')

            mock_learn.assert_called_once_with('rock', 'scissors')

            self.assertEqual(reflect_player.my_prev_move, 'rock')
            self.assertEqual(reflect_player.their_prev_move, 'scissors')


    def test_move(self):
        reflect_player = ReflectPlayer()

        reflect_player.their_prev_move = None
        self.assertEqual(reflect_player.move(), 'rock')

        reflect_player.their_prev_move = 'paper'
        self.assertEqual(reflect_player.move(), 'paper')
