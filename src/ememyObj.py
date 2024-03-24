import basicObj
import pygame
import dataframe

class Enemy(basicObj.Basic):
   def __init__(self) -> None:
      super().__init__("Enemy.png", dataframe.DATA.get("enemy"))

      
