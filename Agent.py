import random as r
from MCTS import MonteCarloTreeSearch


class Agent():
    def __init__(self) -> None:
        pass


class QLearningAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        # n_observations = 16 -- if it was static
        n_action =
        # Need to remember what you need for Q-learning
        pass


class MCTSAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        MCTS = MonteCarloTreeSearch(board)
        move = MCTS.search(1000)
        if move != None:
            return move.actionPlayed


class RandomAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        # Takes in the board class and returns a move
        if board.isLegalMove():
            movesList = board.getPossibleMoves()
            indexOfMove = r.randint(0, len(movesList)-1)
            return movesList[indexOfMove]
        else:
            return None
