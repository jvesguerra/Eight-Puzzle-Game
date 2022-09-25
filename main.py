# References: 
# https://github.com/Gunnar50/SliddingPuzzlePygame
# https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/

import pygame
from sprite import *
from constants import *
from read_grid import *
from search import * # functions
from linked_list import *
from collections import deque


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    #Game Base
    def create_game(self):
        grid_game = input_to_grid()            
        return grid_game

    def create_grid(self):
        for row in range(-1,GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (row, 0),(row, GAME_SIZE * TILESIZE))
        for col in range(-1,GAME_SIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, col),(GAME_SIZE * TILESIZE, col))

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:   # if tile not yet equal to 0 we append to row
                    self.tiles[row].append(Tile(self,col,row,str(tile)))
                else:
                    self.tiles[row].append(Tile(self,col,row,"empty"))   # we would check if tile text == empty or not

    def correct_grid(self):
        c_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return c_grid

    # create the elements in the gui
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()    
        self.tiles_grid_completed = self.correct_grid()             # reference for the winning condition
        self.draw_tiles()

        #Graphics in the game
        self.win = UIElement(90,460,"You Win")
        self.solvable = UIElement2(50,430,"Solvable, You can do this!") 
        self.notSolvable = UIElement2(120,430,"Not Solvable")
        self.button_list = []
        self.button_list.append(Button(150, 530,70,25,"BFS",BLACK))
        self.button_list.append(Button(150, 560,70,25,"DFS",BLACK))

    def run(self):
        self.playing = True     # once we stop this, we will create a new game
        while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()

    def update(self):
        self.all_sprites.update()
          
    def draw(self):
        self.screen.fill(BGCOLOR)                           # background color of the game
        self.all_sprites.draw(self.screen)                  # draw the sprites to the screen
        self.create_grid()
        for button in self.button_list:
            button.draw(self.screen)
        if(self.isSolvable(self.tiles_grid)):
            self.solvable.draw(self.screen)
        else:
            self.notSolvable.draw(self.screen)

        if self.tiles_grid == self.tiles_grid_completed:  # Winning condition
            self.win.draw(self.screen)
        pygame.display.flip()

    def events(self):
        self.action = ""        # saves the action done in the mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks if we clicked the 'x' button
                pygame.quit()
                quit(0)

            #moving the tiles
            if event.type == pygame.MOUSEBUTTONDOWN: # when we click
                mouse_x, mouse_y = pygame.mouse.get_pos() # returns a tuple
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if tile.click(mouse_x, mouse_y):
                            if tile.right() and self.tiles_grid[row][col + 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col] # python swap method
                                self.action = "R"

                            if tile.left() and self.tiles_grid[row][col - 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]
                                self.action = "L"

                            if tile.up() and self.tiles_grid[row - 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]
                                self.action = "U"

                            if tile.down() and self.tiles_grid[row + 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]
                                self.action = "D"

                            self.draw_tiles()
                            print(self.action)

                for button in self.button_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "BFS":
                            self.BFSearch()
                        if button.text == "DFS":
                            pass
    ''' move tiles function
    def moveTiles(self):
        row, col = search(self.tiles_grid,0)
        action_list = actions(self.tiles_grid)
        self.action = ""
        for i in range(0,4):
            self.action = action_list[i]
            print(self.action)

            if self.action == "R":                
                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col] # python swap method

            if self.action == "L":
                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]

            if self.action == "U":
                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]

            if self.action == "D":
                   self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]

            self.draw_tiles()
    '''
    
    #state not updating
    #it does all the action at once
    #saving the last state for the actions
    def result(self,state,action):
        row,col = search(state,0)
        #empty_loc = [row,col]
        if action == "R":                
            state[row][col], state[row][col + 1] = state[row][col + 1], state[row][col] # python swap method

        if action == "L":
            state[row][col], state[row][col - 1] = state[row][col - 1], state[row][col]

        if action == "U":
            state[row][col], state[row - 1][col] = state[row - 1][col], state[row][col]

        if action == "D":
            state[row][col], state[row + 1][col] = state[row + 1][col],state[row][col]

        #print(state)
        return state

    '''
    def BFSearch(self):
        frontier = [self.tiles_grid]
        nodes = linkedList()    # declare linked list
        action_list = actions(self.tiles_grid)
        for i in range(0,len(action_list)):
            if action_list[i] != 0:
                state, empty_loc = self.result(self.tiles_grid,action_list[i])
                print(i)
                #print(state)
                frontier.insert(i,state)
                nodes.insert(state,empty_loc, action_list[i])
                i = i + 1
                #print(frontier)
        #nodes.printLinkedList()
        print(frontier)
    '''
    def BFSearch(self):
        frontier = deque([self.tiles_grid])
        #nodes = linkedList()    # declare linked list
        action_list = actions(self.tiles_grid)
        while(len(frontier)!=0):
            currentState = frontier.popleft()
            print(currentState)
            if goalTest(currentState):
                    return currentState
            else:
                for i in range(0,len(action_list)):    # this for loop would do all the actions
                    if action_list[i] != 0:
                        #pass
                        state = self.result(currentState,action_list[i])
                        print(state)
                        frontier.append(state)
                        #nodes.insert(state,empty_loc, action_list[i])
                        #print(frontier)
                #nodes.printLinkedList()
                print(frontier)
        

    # getInvCount() and isSolvable() checks if the puzzle is solvable
    def getInvCount(self,arr):
        inv_count = 0
        empty_value = 0
        # checks the first value arr[i] is greater than the other values arr[j]
        # if yes, add to inv count
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count
    
    def isSolvable(self,puzzle) :                #If inv_count is true --> the puzzle is solvable else not
        # Count inversions in given 8 puzzle
        inv_count = self.getInvCount([j for sub in puzzle for j in sub])
    
        # return true if inversion count is even.
        return (inv_count % 2 == 0)

game = Game()       # creates game object

while True:
    game.new()
    game.run()

