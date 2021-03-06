# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # This is the starting state of Pacman
    startingNode = problem.getStartState()

    # Check if we are already on a food pellet
    if problem.isGoalState(startingNode):
        return []

    # Use a queue for FIFO
    queue = util.Queue()

    # Use a list to store visited nodes
    explored = []

    # Add starting node and command for Pacman to follow into queue
    queue.push((startingNode, []))

    # While the board is not empty
    while not queue.isEmpty():

        # The node and action that is popped from the queue will be assigned 
        # to the variables currentNode and actions, respectively
        currentNode, actions = queue.pop()

        # If the current node is not already visited, 
        # append the current node to the list of visited nodes
        if currentNode not in explored:
            explored.append(currentNode)

            # If we are at a food pellet, return the actions taken to get to it
            if problem.isGoalState(currentNode):
                return actions

            # If the current node is not the goal, 
            # check the next node and push the next node and action to get to it into the queue
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                queue.push((nextNode, newAction))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
# This is the starting state of Pacman
    startingNode = problem.getStartState()

    # Check if we are already on a food pellet
    if problem.isGoalState(startingNode):
        return []

    # Use a Priority queue for FIFO
    queue = util.PriorityQueue()

    # Use a list to store visited nodes
    explored = []

    # Add starting node and command for Pacman to follow into queue
    #We now need to pass the current cost from start g(n) and the priority number
    queue.push((startingNode, [], 0), 0)

    # While the board is not empty
    while not queue.isEmpty():

        # The node and action that is popped from the queue will be assigned 
        # to the variables currentNode and actions, respectively
        currentNode, actions, currentCost = queue.pop()

        # If the current node is not already visited, 
        # append the current node to the list of visited nodes
        if currentNode not in explored:
            explored.append(currentNode)

            # If we are at a food pellet, return the actions taken to get to it
            if problem.isGoalState(currentNode):
                return actions

            # If the current node is not the goal, 
            # check the next node and push the next node and action to get to it into the queue
            # we can now use the cost
            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                #g(n) is cumulative
                updatedCost = currentCost + cost
                #get priority based on heurstic h(n)
                #heursitc = node + 5
                priority = updatedCost + heuristic(nextNode, problem)
                queue.push((nextNode, newAction, updatedCost), priority)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
