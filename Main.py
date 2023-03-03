# All inital set up
from Board import Board
from Agent import *
import copy
import csv
from QLearningAlgorithm import QLearning

from Environment import Environment

# Want to write some code that goes over all of this and i want it to run over the diffrerent models and at the end record the scores

while True:
    print('Welcome to 2048 Game')
    print('Select a who you want to play:')
    print('1. You play youself -- arrow keys control')
    print('2. Random agent')
    print('3. Monte Carlo Tree Search Agent')
    print('4. Q-Learning')
    print('5. MiniMax')
    print('6. Train Q-learning Model')
    print('7 Get all the data in one')
    userInput = input()

    if userInput == '1':
        env = Environment()
        temp, numberOfMoves = env.runHuman()
    elif userInput == '2':
        env = Environment(RandomAgent())
        temp, numberOfMoves = env.runAgent()
    elif userInput == '3':
        env = Environment(MCTSAgent())
        temp, numberOfMoves = env.runAgent()
    elif userInput == '4':
        env = Environment(QLearningAgent())
        temp, numberOfMoves = env.runAgent()
    elif userInput == '5':
        env = Environment(MiniMaxAgent())
        temp, numberOfMoves = env.runAgent()
    elif userInput == '6':
        # Train the model
        state = Board()
        q_learning = QLearning()
        q_learning.train(state)
    elif userInput == '7':
        gameData = []
        # What is playing, number of moves, highest tile, score

        for i in range(0, 10):
            env = Environment()
            temp, numberOfMoves = env.runHuman()
            highestTile, score = temp.boardForData()
            gameData.append(['Human', numberOfMoves, highestTile, score])

        for i in range(0, 10):
            randomEnv = Environment(RandomAgent())
            temp, numberOfMoves = randomEnv.runAgent()
            highestTile, score = temp.boardForData()
            gameData.append(
                ['Random Agent', numberOfMoves, highestTile, score])

        for i in range(0, 10):
            mctsEnv = Environment(MCTSAgent())
            temp, numberOfMoves = mctsEnv.runAgent()
            highestTile, score = temp.boardForData()
            gameData.append(
                ['MCTS Agent', numberOfMoves, highestTile, score])

        for i in range(0, 10):
            q_learningEnv = Environment(QLearningAgent())
            temp, numberOfMoves = q_learningEnv.runAgent()
            highestTile, score = temp.boardForData()
            gameData.append(
                ['Q-Learning Agent', numberOfMoves, highestTile, score])

        # for i in range(0, 10):
        #     miniMaxEnv = Environment(MiniMaxAgent())
        #     temp, numberOfMoves = miniMaxEnv.runAgent()
        #     highestTile, score = temp.boardForData()
        #     gameData.append(
        #         ['MiniMax Agent', numberOfMoves, highestTile, score])

        header = ["Player", 'Number of Moves', 'Highest Tile', 'Score']
        with open('game_data.csv', 'w') as f:
            writer = csv.writer(f)

            writer.writerow(header)
            writer.writerows(gameData)
    else:
        print('Please enter a number from he options above')
