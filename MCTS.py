import numpy as np
import copy
import random as r


class MonteCarloTreeSearch():
    def __init__(self, state):
        self.root = Node(state)

    def search(self, n):
        """Runs the 4 phaswes of the MCTS algorithm and at the end picks the best actoin


        n - number of iteractions
        """
        for i in range(0, n):
            print(i)
            node = self.treePolicy()
            reward = node.simulation()
            node.backpropagate(reward)
        return self.root.UCT()

    def treePolicy(self):
        currentNode = self.root
        while not currentNode.terminalNode():
            if not currentNode.isFullyExpanded():
                return currentNode.expand()
            else:
                currentNode = currentNode.UCT()
        return currentNode

    # Could write a second tree policy that looks at the current score


class Node():
    def __init__(self, state, parent=None, actionPlayed=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.numberOfVisits = 0
        self.numberOfWins = 0
        self.actionPlayed = actionPlayed

    @property
    def untriedAction(self):
        if not hasattr(self, '_untriedActions'):
            self.__untriedActions = self.state.getPossibleMoves()
        return self.__untriedActions

    def n(self):
        return self.numberOfVisits

    def w(self):
        return self.numberOfWins

    def expand(self):
        """State is copied and action picked from list, this is then performed on new state is created, this is then aded ot the child list and returned"""
        newState = copy.deepcopy(self.state)
        action = self.untriedAction.pop()
        newState.move(action)
        childNode = Node(newState, parent=self, actionPlayed=action)
        self.children.append(childNode)
        return childNode

    def terminalNode(self):
        return self.state.isGameOver()

    def simulation(self):
        rolloutState = copy.deepcopy(self.state)

        while True:
            potencialMoves = rolloutState.getPossibleMoves()
            if len(potencialMoves) == 0:
                return 0

            action = self.rolloutPolicy(potencialMoves)
            rolloutState.move(potencialMoves[action])
            if rolloutState.isGameOver():
                if '2048' in rolloutState.board:
                    return 1
                else:
                    return 0

    def rolloutPolicy(self, potencialMoves):
        return r.randint(0, len(potencialMoves)-1)

    def backpropagate(self, simulationResult):
        self.numberOfVisits += 1
        self.numberOfWins += simulationResult
        if self.parent:
            self.parent.backpropagate(simulationResult)

    def isFullyExpanded(self):
        return len(self.untriedAction) == 0

    def UCT(self, c=1.6):

        uctScore = [(child.w() / (child.n())) + c * np.sqrt((2 *
                                                             np.log(self.n()) / (child.n()))) for child in self.children]

        try:
            index = np.argmax(uctScore)

            return self.children[index]
        except Exception:
            return None
