import pygame
import data
def draw(path,size,location):
    if path == "None":
        return
    path = f"./app_data/image/source/{path}"
    image = pygame.image.load(path)
    original_width, original_height = image.get_size()
    scale_width = size[0] / original_width
    scale_height = size[1] / original_height
    scale = max(scale_width, scale_height)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    resized_image = pygame.transform.scale(image,(new_width,new_height))
    if location == (-1,-1):
        data.screen.blit(resized_image,((data.screen.get_width() - new_width) / 2,(data.screen.get_height() - new_height) / 2))
    else:
        data.screen.blit(resized_image,location)
class New:
    def __init__(self):
        self.image = None
        self.location = None
    def set(self,path,size,location):
        if path == "None":
            self.image = None
            self.location = None
            return
        path = f"./app_data/image/source/{path}"
        image = pygame.image.load(path)
        original_width, original_height = image.get_size()
        scale_width = size[0] / original_width
        scale_height = size[1] / original_height
        scale = max(scale_width, scale_height)
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        self.image = pygame.transform.smoothscale(image,(new_width,new_height))
        if location == (-1,-1):
            self.location = ((data.screen.get_width() - new_width) / 2,(data.screen.get_height() - new_height) / 2)
        else:
            self.location = location
    def draw(self):
        if self.image == None or self.location == None:
            return
        data.screen.blit(self.image,self.location)
    def get_size(self):
        if self.image:
            return self.image.get_size()
        else:
            return (0,0)
    def get_location(self):
        if self.location:
            return self.location
        else:
            return (0,0)