import pygame
from color import Color
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.colors = Color.get_color_list()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state >= len(self.cells):
            self.rotation_state = 0
    
    def undo_rotate(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y, alpha=255):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + offset_x, tile.row * self.cell_size + offset_y, self.cell_size - 1, self.cell_size - 1)
            color = self.colors[self.id]
            if alpha < 255:
                # Create a transparent color (R, G, B, A)
                transparent_color = (*color[:3], alpha)
                # Create a transparent surface
                transparent_surface = pygame.Surface((self.cell_size - 1, self.cell_size - 1), pygame.SRCALPHA)
                transparent_surface.fill(transparent_color)  # Fill with transparent color
                screen.blit(transparent_surface, tile_rect.topleft)
            else:
                # Draw normally if no transparency is needed
                pygame.draw.rect(screen, color, tile_rect)
    

    
