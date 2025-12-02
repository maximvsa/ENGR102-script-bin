# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Maximus Amick
#               Daniel Yoo
#               Caleb Carter
#               Noah Kim
# Section:      513
# Assignment:   Lab: Topic 13 (team)
# Date:         5 December 2025

import pygame

class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

def main():
    pygame.init()
    pygame.font.init()
    
    screen_width = 1200
    screen_height = 900
    
    pastel_yellow = (253, 253, 150)
    pastel_red = (255, 105, 97)
    pastel_blue = (174, 198, 207)
    pastel_green = (119, 221, 119)
    pastel_orange = (255, 179, 71)
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("FLIP 7")
    
    background_rect = pygame.Rect(0, 0, screen_width, screen_height)
    
    title_font = pygame.font.SysFont("Helvetica", 400)
    controls_font = pygame.font.SysFont("LMAO", 50)
    player_text_font = pygame.font.SysFont("Helvetica", 50)
    
    title_surface = title_font.render("FLIP 7", True, (0, 0, 0))
    title_text_rect = title_surface.get_rect()
    title_text_rect.center = (screen_width // 2, 200)
    
    controls_background_rect = pygame.Rect(0, screen_height - 40, screen_width, 40)
    controls_surface = controls_font.render("[SPACE]-Continue  [H]-Hit  [S]-Stay  [TAB]-Scores  [R]-Rules", True, (255, 255, 255))
    controls_text_rect = controls_surface.get_rect()
    controls_text_rect.center = (screen_width // 2, screen_height - 20)
    
    player1_text_surface = player_text_font.render("Player 1:", True, (0, 0, 0))
    player1_text_rect = player1_text_surface.get_rect()
    
    player2_text_surface = player_text_font.render("Player 2:", True, (0, 0, 0))
    player2_text_rect = player1_text_surface.get_rect()
    
    player3_text_surface = player_text_font.render("Player 3:", True, (0, 0, 0))
    player3_text_rect = player1_text_surface.get_rect()
    
    player3_text_rect.bottomleft = (10, controls_background_rect.topleft[1] - 150)
    player2_text_rect.bottomleft = (10, player3_text_rect.topleft[1] - 150)
    player1_text_rect.bottomleft = (10, player2_text_rect.topleft[1] - 150)
    
    round_number = 0
    game_state = "title screen"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == "title screen":
                    if event.key == pygame.K_SPACE:
                        game_state = "between rounds"
                        player1 = Player()
                        player2 = Player()
                        player3 = Player()
                        round_number = 1
        
        if game_state == "title screen":
            pygame.draw.rect(screen, pastel_yellow, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(title_surface, title_text_rect)
        
        if game_state == "between rounds":
            pygame.draw.rect(screen, pastel_yellow, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(player1_text_surface, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()