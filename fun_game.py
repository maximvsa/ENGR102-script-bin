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
import random

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
    rules_font = pygame.font.SysFont("Helvetica", 32)
    deck_card_count_font = pygame.font.SysFont("Helvetica", 24)
    card_font = pygame.font.SysFont("Helvetica", 32)
    
    title_surface = title_font.render("FLIP 7", True, (0, 0, 0))
    title_text_rect = title_surface.get_rect()
    title_text_rect.center = (screen_width // 2, 200)
    
    controls_background_rect = pygame.Rect(0, screen_height - 40, screen_width, 40)
    controls_surface = controls_font.render("[SPACE]-Continue  [H]-Hit  [S]-Stay  [TAB]-Scores  [R]-Rules", True, (255, 255, 255))
    controls_text_rect = controls_surface.get_rect()
    controls_text_rect.center = (screen_width // 2, screen_height - 20)
    
    rules_overlay_rect = pygame.Rect(screen_width // 2 - 400, screen_height // 2 - 220, 800, 440)
    rules_lines = [
        "Flip 7 Overview",
        "- Goal: finish closest to 7 without going over.",
        "- Draw (Hit) or Hold (Stay) on your turn.",
        "- Number cards are worth their face value.",
        "- You lose the round if you bust above 7.",
        "- After each round, press SPACE to continue."
    ]
    
    player1_text_surface = player_text_font.render("Player 1:", True, (0, 0, 0))
    player1_text_rect = player1_text_surface.get_rect()
    
    player2_text_surface = player_text_font.render("Player 2:", True, (0, 0, 0))
    player2_text_rect = player1_text_surface.get_rect()
    
    player3_text_surface = player_text_font.render("Player 3:", True, (0, 0, 0))
    player3_text_rect = player1_text_surface.get_rect()
    
    player3_text_rect.bottomleft = (10, controls_background_rect.topleft[1] - 150)
    player2_text_rect.bottomleft = (10, player3_text_rect.topleft[1] - 150)
    player1_text_rect.bottomleft = (10, player2_text_rect.topleft[1] - 150)
    
    # Deck Composition
    global deck
    deck = [0]
    for i in range(1, 13):
        for _ in range(i):
            deck.append(i)
    deck.append("+2")
    deck.append("+4")
    deck.append("+6")
    deck.append("+8")
    deck.append("+10")
    
    
    # Deck Rectangle for display in top right
    deck_rect = pygame.Rect(screen_width - 150, 50, 100, 150)
    deck_surface = pygame.Surface((deck_rect.width, deck_rect.height))
    deck_surface.fill((200, 200, 200))
    pygame.draw.rect(deck_surface, (0, 0, 0), deck_surface.get_rect(), 4)
    
    def draw_deck_info(target_surface):
        target_surface.blit(deck_surface, deck_rect)
        deck_card_count_surface = deck_card_count_font.render(f"Cards: {len(deck)}", True, (0, 0, 0))
        deck_card_count_rect = deck_card_count_surface.get_rect()
        deck_card_count_rect.center = (deck_rect.centerx, deck_rect.bottom + 20)
        target_surface.blit(deck_card_count_surface, deck_card_count_rect)
    
    card_colors = {
        "player1": (255, 255, 255),
        "player2": (240, 240, 240),
        "player3": (225, 225, 225),
    }
    card_width = 80
    card_height = 120
    card_spacing = 12
    card_gap = 15
    
    def draw_player_hand(target_surface, player, label_rect, player_key):
        if not player or not player.hand:
            return
        x = label_rect.left
        y = label_rect.bottom + card_gap
        for card in player.hand:
            card_rect = pygame.Rect(x, y, card_width, card_height)
            pygame.draw.rect(target_surface, card_colors[player_key], card_rect)
            pygame.draw.rect(target_surface, (0, 0, 0), card_rect, 2)
            value_surface = card_font.render(str(card), True, (0, 0, 0))
            value_rect = value_surface.get_rect()
            value_rect.center = card_rect.center
            target_surface.blit(value_surface, value_rect)
            x += card_width + card_spacing
    
    game_over = False
    
    player1 = None
    player2 = None
    player3 = None
    
    round_number = 0
    game_state = "title screen"
    rules_visible = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rules_visible = True
                if game_state == "title screen":
                    if event.key == pygame.K_SPACE:
                        game_state = "between rounds"
                        player1 = Player()
                        player2 = Player()
                        player3 = Player()
                elif game_state == "between rounds":
                    if event.key == pygame.K_SPACE:
                        round_number += 1
                        game_state = "player 1 turn"
                elif game_state == "player 1 turn":
                    if event.key == pygame.K_h:
                        player1.hand.append(deck.pop())
                    elif event.key == pygame.K_s:
                        game_state = "player 2 turn"
                elif game_state == "player 2 turn":
                    if event.key == pygame.K_h:
                        player2.hand.append(deck.pop())
                    elif event.key == pygame.K_s:
                        game_state = "player 3 turn"
                elif game_state == "player 3 turn":
                    if event.key == pygame.K_h:
                        player3.hand.append(deck.pop())
                    elif event.key == pygame.K_s:
                        game_state = "between rounds"
                
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    rules_visible = False
        
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
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            
            random.shuffle(deck)
        
        if game_state == "player 1 turn":
            pygame.draw.rect(screen, pastel_red, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(player1_text_surface, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            
            

        if rules_visible:
            overlay_surface = pygame.Surface((rules_overlay_rect.width, rules_overlay_rect.height), pygame.SRCALPHA)
            overlay_surface.fill((0, 0, 0, 200))
            pygame.draw.rect(overlay_surface, (255, 255, 255), overlay_surface.get_rect(), 4)
            
            text_y = 30
            for line in rules_lines:
                line_surface = rules_font.render(line, True, (255, 255, 255))
                line_rect = line_surface.get_rect()
                line_rect.centerx = overlay_surface.get_rect().width // 2
                line_rect.y = text_y
                overlay_surface.blit(line_surface, line_rect)
                text_y += 60 if line.startswith("-") else 50
            
            # Center the overlay each frame so it stays anchored even if the window changes later.
            overlay_dest = overlay_surface.get_rect()
            overlay_dest.center = (screen_width // 2, screen_height // 2)
            screen.blit(overlay_surface, overlay_dest)
        
        if not game_over and player1 and player2 and player3:
            if player1.score >= 200 or player2.score >= 200 or player3.score >= 200:
                game_over = True
        
        if game_over:
            
            game_state = "game over"
            # Determine winner
            
            scores = [player1.score, player2.score, player3.score]
            max_score = max(scores)
            winner = scores.index(max_score) + 1
            
            # Draw Game Over screen
            pygame.draw.rect(screen, pastel_orange, background_rect)
            game_over_font = pygame.font.SysFont("Helvetica", 150)
            game_over_surface = game_over_font.render(f"GAME OVER. Player {winner} is the 67 chungus queen of Ohio", True, (0, 0, 0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.center = (screen_width // 2, screen_height // 2)
            screen.blit(game_over_surface, game_over_rect)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()