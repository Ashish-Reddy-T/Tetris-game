import pygame, random, time
from grid import Grid
from blocks import *

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.high_score = 0

        self.transparent_timer = 0
        self.transparent_duration = 1
        self.is_transparent = False

        self.rotate_sound = pygame.mixer.Sound('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Rotate Sound.ogg')
        self.clear_sound = pygame.mixer.Sound('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Clear Sound for Tetris.ogg')

        pygame.mixer.music.load('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Tetris Game Music.ogg')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    
    def update_score(self, lines_cleared, moved_down_points):
        if lines_cleared == 1:
            self.score += 100
            self.check_for_high_score()
        elif lines_cleared == 2:
            self.score += 300
            self.check_for_high_score()
        elif lines_cleared == 3:
            self.score += 500
            self.check_for_high_score()
        self.score += moved_down_points
        self.check_for_high_score()
    
    def get_random_block(self):
        if not self.blocks:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block


    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside(self.current_block) or not self.block_fits(self.current_block):
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside(self.current_block) or not self.block_fits(self.current_block):
            self.current_block.move(0, -1)
    
    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside(self.current_block) or not self.block_fits(self.current_block):
            self.current_block.move(-1, 0)
            if not self.is_transparent:
                # Start transparency timer
                self.is_transparent = True
                self.transparent_timer = time.time()
            else:
                # Check if the transparency duration has passed
                if time.time() - self.transparent_timer >= self.transparent_duration:
                    self.lock_block()
                    self.is_transparent = False
        else:
            self.is_transparent = False
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id 
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if not self.block_fits():
            self.game_over = True


    def block_fits(self, block=None):
        if block is None:
            block = self.current_block
        tiles = block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):  # Check if tile is inside the grid
                return False
            if not self.grid.is_empty(tile.row, tile.column):  # Check if the cell is empty
                return False
        return True
    
    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside(self.current_block) or not self.block_fits(self.current_block):
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()

    def block_inside(self, block):
        tiles = block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 250)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 237)
        else:
            self.next_block.draw(screen, 270, 230)

    def reset(self):
        self.grid.reset()
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        pygame.mixer.music.load('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Tetris game/Tetris Game Music.ogg')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    
    def check_for_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
    
    def draw_ghost_block(self, screen):
        ghost_block = self.current_block
        # Create a copy of the current block to avoid modifying the original
        ghost_block = type(self.current_block)()
        ghost_block.row_offset = self.current_block.row_offset
        ghost_block.column_offset = self.current_block.column_offset
        ghost_block.rotation_state = self.current_block.rotation_state

        # Move the ghost block down until it can't move further
        while True:
            ghost_block.move(1, 0)
            if not self.block_inside(ghost_block) or not self.block_fits(ghost_block):
                ghost_block.move(-1, 0)
                break

        # Draw the ghost block with reduced transparency
        ghost_block.draw(screen, 11, 11, alpha=128)


        