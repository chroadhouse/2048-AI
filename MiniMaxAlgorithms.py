import numpy as np
import copy as c
import random as r


class MiniMax():
    def __init__(self) -> None:
        pass

    def evaluate(self, state):
        # This needs to be changed
        return state.score

    def search(self, state, max_depth):
        stack = [(state, 0, None)]
        best_move = None
        best_utility = float('-inf')

        while stack:
            popState, depth, last_move = stack.pop()
            if depth == max_depth or popState.isGameOver():
                utility = self.evaluate(popState)
                if utility > best_utility:
                    best_move = last_move
                    best_utility = utility
                continue

                # Generate children
            for move in popState.getPossibleMoves():
                child = c.deepcopy(popState)
                child.move(move)
                stack.append((child, depth+1, move))

        return best_move, best_utility
