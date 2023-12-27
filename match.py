#!/usr/bin/env python3

import random
from itertools import islice, cycle


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def random_move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return self.random_move()


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("What is your move?\n")
            if move in moves:
                return move
            else:
                print(f'Oops {move} is not a valid option')


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return self.random_move()
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None
        self.index = None
        self.moves_iterator = islice(cycle(moves), self.index, None)

    def move(self):
        if self.my_move is None:
            move = self.random_move()
            self.index = moves.index(move) + 1
            self.moves_iterator = islice(cycle(moves), self.index, None)
            return move
        else:
            return next(self.moves_iterator)

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tie(one, two):
    return ((one == 'rock' and two == 'rock') or
            (one == 'scissors' and two == 'scissors') or
            (one == 'paper' and two == 'paper'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins\n")
            self.p1_score += 1
        elif tie(move1, move2):
            print("It is a tie\n")
        else:
            print("Player 2 wins\n")
            self.p2_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!\n")
        print(self.final_score())

    def final_score(self):
        print(f'Final score:\nPlayer 1: {self.p1_score} - Player 2: \
{self.p2_score}')
        if self.p1_score > self.p2_score:
            return "Player 1 wins!"
        if self.p1_score < self.p2_score:
            return "Player 2 wins!"
        else:
            return "It is a tie!"


if __name__ == '__main__':
    game = Game(RandomPlayer(), ReflectPlayer())
    game.play_game()
