from search import search

class StateNode:
    def __init__(self, puzzle, action, parent):
        self.puzzle = puzzle
        self.empty_loc = 0
        self.action = action
        self.parent = parent