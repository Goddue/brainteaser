import pygame
from random import choice


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_image, pos_x, pos_y, *group):
        super().__init__(*group)
        # Выберается не конкретное, а случайное изображение, чтобы ранообразить тайлсет
        self.image = choice(tile_image)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.abs_pos = self.rect.x, self.rect.y