import time
from tqdm import tqdm
from PIL import Image
import os
class sleeper():
   def __init__(self, image, source_card1, descripton) -> None:
      self.image = image
      self.source_card1 = source_card1
      self.descripton = descripton
      self.out                     = Image.alpha_composite(self.image,self.source_card1)
      mylist = [1]
      for i in tqdm(mylist,desc=self.descripton):

         self.out.save("output/save.png")
