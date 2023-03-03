import random as r
from MCTS import MonteCarloTreeSearch
from MiniMaxAlgorithms import MiniMax
from QLearningAlgorithm import QLearning
import pickle


class Agent():
    def __init__(self) -> None:
        pass


class QLearningAgent(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.q_table = None

    def act(self, board):
        # n_observations = 16 -- if it was static
        # n_action = Number of posible action s- should be 4
        # Need to remember what you need for Q-learning
        if self.q_table == None:
            self.pullTable()

        # print(self.q_table)

        move = self.getBestMove(board)
        return move

    def getBestMove(self, state):
        best_move = None
        best_q_value = float('-inf')
        for move in state.getPossibleMoves():
            q_value = self.q_table.get((tuple(state.getState()), move), 0)
            if q_value > best_q_value:
                best_move = move
                best_q_value = q_value

        if best_move == None:
            print('whoops')
            if state.isLegalMove():
                movesList = state.getPossibleMoves()
                indexOfMove = r.randint(0, len(movesList)-1)
            return movesList[indexOfMove]
        return best_move

    def pullTable(self):
        with open('q_table.pickle', 'rb') as f:
            self.q_table = pickle.load(f)
            print('data loaded')


class MCTSAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        MCTS = MonteCarloTreeSearch(board)
        move = MCTS.search(50)
        if move != None:
            print(f'Move Selected: {move.actionPlayed}')
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


class MiniMaxAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        miniMax = MiniMax()
        move, _ = miniMax.search(board, 5)
        print(f'Move is {move}')
        if move != None:
            print(f'Move Selected: {move}')
            return move
        else:
            print('you have fuycked it')


class AlphaBetaAgent(Agent):
    def __init__(self) -> None:
        super().__init__()

    def act(self, board):
        pass
