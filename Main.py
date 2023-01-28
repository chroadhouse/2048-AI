# All inital set up
from Board import Board
from Agent import *
import pygame
import copy

from Environment import Environment


while True:
    print('Welcome to 2048 Game')
    print('Select a who you want to play:')
    print('1. You play youself -- arrow keys control')
    print('2. Random agent')
    print('3. Monte Carlo Tree Search Agent')
    print('4. Q-Learning')
    userInput = input()

    if userInput == '1':
        env = Environment()
        env.runHuman()
    elif userInput == '2':
        env = Environment(RandomAgent())
        env.runAgent()
    elif userInput == '3':
        env = Environment(MCTSAgent())
        env.runAgent()
    else:
        print('Please enter a number from he options above')
