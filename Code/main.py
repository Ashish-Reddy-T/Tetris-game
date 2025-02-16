import pygame, sys
from game import Game
from color import Color

pygame.init()

title_font = pygame.font.Font('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Space Invaders game/Monogram Font.ttf', 40)
score_surface = title_font.render('Score', True, Color.white)
next_surface = title_font.render('Next', True, Color.white)
game_over_surface = title_font.render('GAME OVER', True, Color.white)
high_score_surface = title_font.render('High Score: ', True, Color.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 175, 170, 180)
high_score_rect = pygame.Rect(320, 425, 170, 60)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption('Tetris!')

game = Game()


GAME_EVENT = pygame.USEREVENT
pygame.time.set_timer(GAME_EVENT, 1000) 

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and not game.game_over:
                game.move_left()
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and not game.game_over:
                game.move_right()
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and not game.game_over:
                game.rotate()
        if event.type == GAME_EVENT and not game.game_over:
            game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Color.white)
    high_score_value_surface = title_font.render(str(game.high_score), True, Color.white)
    high_score_value_rect = high_score_value_surface.get_rect(center = high_score_rect.center)

    screen.fill(Color.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 140, 50, 50))
    screen.blit(high_score_surface, (328, 385, 50, 50))

    pygame.draw.rect(screen, Color.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Color.light_blue, high_score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    screen.blit(high_score_value_surface, high_score_value_rect)

    pygame.draw.rect(screen, Color.light_blue, next_rect, 0, 10)
    game.draw(screen)

    game.draw_ghost_block(screen)
    if game.is_transparent:
        game.current_block.draw(screen, 11, 11, alpha = 128)
    else:
        game.current_block.draw(screen, 11, 11)

    if game.game_over:
        
        overlay = pygame.Surface((500, 620), pygame.SRCALPHA)
        overlay.fill((0,0,0,128))

        game_over_text = pygame.font.Font('/Users/AshishR_T/Desktop/Timepass python projects/Python games/Space Invaders game/Monogram Font.ttf', 60).render('GAME OVER', True, Color.white)
        game_over_rect = game_over_text.get_rect(center = (250, 250))

        instruction_font = pygame.font.Font(None, 25)
        instruction1 = instruction_font.render('SPACE to Play Again   [OR]', True, Color.white)
        instruction2 = instruction_font.render('ESCAPE to Exit', True, Color.white)

        instruction1_rect = instruction1.get_rect(center = (250, 300))
        instruction2_rect = instruction2.get_rect(center = (250, 330))

        overlay.blit(game_over_text, game_over_rect)
        overlay.blit(instruction1, instruction1_rect)
        overlay.blit(instruction2, instruction2_rect)

        screen.blit(overlay, (0, 0))
        pygame.mixer.music.stop()
    
    

    pygame.display.update()
    clock.tick(60)