import basicObj
import pygame
import const
import dataframe
import time
import random

class Enemy(basicObj.Basic):
   def __init__(self) -> None:
      super().__init__("Enemy.png", dataframe.DATA.get("enemy"))
      self.level = 0
      self.rand_flag = random.randint(0,1)
      self.preframe_time = 0
   
   def levelUp(self):
      self.level += 1
      self.speed_fwd += 1
      self.speed_lt += 1
      self.speed_rt += 1

   def levelDown(self):
      if self.level > -4:
         self.level -= 1
         self.speed_fwd -= 1
         self.speed_lt -= 1
         self.speed_rt -= 1

   def reset(self):
      if (self.rect.top > const.SCREEN_HEIGHT):
         self.rect.top = 0
         self.rect.center = (random.randint(30,370), 0)

   def moveWithFrame(self,drunk:bool):
      if time.time() - self.preframe_time <= 45/const.FPS_LIMIT:
         if drunk:
            if self.rand_flag == 1:
               if self.rect.left > 0:
                  self.goFwd(mirror=True)
                  self.goLt()
               else:
                  self.rand_flag = 0
                  self.goFwd(mirror=True)
            else:
               if self.rect.right < const.SCREEN_WIDTH:
                  self.goFwd(mirror=True)
                  self.goRt()
               else:
                  self.rand_flag = 1
                  self.goFwd(mirror=True)
         else:
            self.goFwd(mirror=True)
         self.reset()
         return
      self.preframe_time = time.time()
      self.rand_flag = random.randint(0,1)
      self.goFwd(mirror=True)
      self.reset()
      return

      


   
   

   
      
