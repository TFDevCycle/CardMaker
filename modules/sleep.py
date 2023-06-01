import time
from tqdm import tqdm
from PIL import Image
import os
import re
class sleeper():
   def __init__(self, image, title, source_card1, descripton) -> None:
      self.image = image
      self.title = title
      self.source_card1 = source_card1
      self.descripton = descripton
      self.out                     = Image.alpha_composite(self.image,self.source_card1)
      mylist = [1]
      for i in tqdm(mylist,desc=self.descripton):

         self.out.save("output/save.png")

         self.file_name = re.sub(r"[^a-zA-Z0-9 | ]*","", self.title).replace(" ", "_")+'.png'
         self.out.save("output/" + self.file_name)
