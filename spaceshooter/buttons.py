import pygame
from os.path import join

class Button:
    def __init__(self, image_path, image_size, image_position):
        image_path = pygame.image.load(image_path)
        self.x = image_position[0]
        self.y = image_position[1]
        self.width = image_size[0]
        self.height = image_size[1]
        image_transform = pygame.transform.scale(image_path, (self.width,self.height)).convert_alpha()
        self.image = image_transform
        self.rect = self.image.get_rect(center=(self.x,self.y))
        #self.rect.topleft = (x, y)

    # def check_click(self, mouse_pos):
    #     """Check if the button was clicked."""
    #     mouse_x, mouse_y = mouse_pos
    #     if (self.image_position[0] <= mouse_x <= self.image_position[0] + self.image_size[0] and
    #         self.image_position[1] <= mouse_y <= self.image_position[1] + self.image_size[1]):
    #         return True
    #     return False    # def update(self,screen):
    #     screen.blit(self.image,self.rect)

def check_click(button, mouse_pos):
    """Check if the button was clicked."""
    mouse_x, mouse_y = mouse_pos
    if (button.x <= mouse_x <= button.x + button.width and
        button.y <= mouse_y <= button.y + button.height):
        return True
    return False
# Load play button 
