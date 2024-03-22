import random as r 
import pygame as pg 

class Inimigo(pg.sprite.Sprite) :
    def __init__(self, pos, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center= pos 
    def move(self, )
        
             