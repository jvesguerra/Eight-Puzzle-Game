from turtle import width
import pygame
from constants import *

pygame.font.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups) # calling constructor
        self.game = game
        self.x, self.y = x,y
        self.text = text
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        if self.text != "empty":
            self.font = pygame.font.SysFont("Consolas", 50)
            font_surface = self.font.render(self.text, True, BLACK)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)
            center_x = (TILESIZE/2) - self.font_size[0]/2
            center_y = (TILESIZE/2) - self.font_size[1]/2
            self.image.blit(font_surface, (center_x, center_y))
        else:
            self.image.fill(BGCOLOR)

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def click(self, mouse_x, mouse_y): 
        return self.rect.left <= mouse_x <= self.rect.right and self.rect.top <= mouse_y <= self.rect.bottom  # to check if its in the tile

    def right(self):
        return self.rect.x + TILESIZE < GAME_SIZE * TILESIZE

    def left(self):
        return self.rect.x - TILESIZE >= 0

    def down(self):
        return self.rect.y + TILESIZE < GAME_SIZE * TILESIZE

    def up(self):
        return self.rect.y - TILESIZE >= 0

#To draw elements in the gui

class UIElement:
    def __init__(self,x,y, text):
        self.x, self.y = x,y
        self.text = text
    
    def draw(self,screen):
        font = pygame.font.SysFont("Consolas", 50)
        text = font.render(self.text, True, WHITE)
        screen.blit(text,(self.x,self.y))

class UIElement2:
    def __init__(self,x,y, text):
        self.x, self.y = x,y
        self.text = text
    
    def draw(self,screen):
        font = pygame.font.SysFont("Consolas", 20)
        text = font.render(self.text, True, WHITE)
        screen.blit(text,(self.x,self.y))

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.color = color
        self.width, self.height = width, height
        self.x, self.y = x,y
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("Consolas",15)
        text = font.render(self.text, True, WHITE)
        self.font_size = font.size(self.text)
        center_x = self.x + (self.width/2) - self.font_size[0]/2
        center_y = self.y + (self.height/2) - self.font_size[1]/2
        screen.blit(text, (center_x, center_y))

    def click(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height