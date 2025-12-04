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
        self.stayed = False
        self.busted = False
        self.hit_this_turn = False
        self.status_text = ""
        self.first_turn_completed = False
        self.round_points_awarded = False

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
    rules_font = pygame.font.SysFont("Helvetica", 22)
    scoreboard_font = pygame.font.SysFont("Helvetica", 40)
    small_score_font = pygame.font.SysFont("Helvetica", 28)
    deck_card_count_font = pygame.font.SysFont("Helvetica", 24)
    card_font = pygame.font.SysFont("Helvetica", 32)
    info_font = pygame.font.SysFont("Helvetica", 28)
    status_font = pygame.font.SysFont("Helvetica", 24)
    
    title_surface = title_font.render("FLIP 7", True, (0, 0, 0))
    title_text_rect = title_surface.get_rect()
    title_text_rect.center = (screen_width // 2, 200)
    
    controls_background_rect = pygame.Rect(0, screen_height - 40, screen_width, 40)
    controls_surface = controls_font.render("[SPACE]-Continue  [H]-Hit  [S]-Stay  [TAB]-Scores  [R]-Rules", True, (255, 255, 255))
    controls_text_rect = controls_surface.get_rect()
    controls_text_rect.center = (screen_width // 2, screen_height - 20)
    
    rules_overlay_rect = pygame.Rect(screen_width // 2 - 500, screen_height // 2 - 320, 1000, 640)
    rules_paragraphs = [
        "Flip 7: Full Table Rules",
        "Objective: Build a hand whose total is as close as possible to 7 without exceeding it. First player to accumulate 200 total points wins the crown.",
        "Turn Entry: When your turn begins you must take exactly one Hit. The new card immediately joins your hand and becomes eligible for duplicate checks.",
        "Duplicate Penalty: If the card you drew already exists anywhere in your hand, you bust instantly. Busted players are out for the round and forfeit any new points from that hand.",
        "Staying: After you complete the mandatory opening Hit, later turns let you choose Stay. Staying banks your hand total right away and marks you “out” for the rest of the round.",
        "Second Hits: Future visits to your turn still obey the “one Hit per visit” rule. You can alternate between Hit and Stay decisions as long as you have not busted or stayed already.",
        "Scoring: Your round total equals the sum of every card in your hand (+ cards count as bonuses). Totals higher than 7 simply mean you busted and earn zero new points.",
        "Ties & Points: If multiple players end near 7, feel free to award style points verbally, but numerically you only keep what you banked when staying.",
        "Round End: The round ends once every player has either Stayed or Busted. SPACE on the between-rounds screen shuffles a fresh deck and begins the next round.",
        "Deck Reset: Each deck contains integers 0 through 12 with frequency matching the face value plus the +2/+4/+6/+8/+10 bonus cards.",
        "Overlays: Hold R for these rules, TAB for the scoreboard, or hold both keys to view both overlays at once.",
        "Controls Recap: SPACE advances prompts, H performs your single hit for the turn, S stays (after your first hit), TAB shows scores, and R shows rules.",
        "Sportsmanship: Declare dramatic victories, gracious defeats, and remember—Aggies do not cheat."
    ]
    
    scoreboard_overlay_rect = pygame.Rect(screen_width // 2 - 350, screen_height // 2 - 200, 700, 400)
    
    player1_text_surface = player_text_font.render("Player 1:", True, (0, 0, 0))
    player1_text_rect = player1_text_surface.get_rect()
    
    player2_text_surface = player_text_font.render("Player 2:", True, (0, 0, 0))
    player2_text_rect = player1_text_surface.get_rect()
    
    player3_text_surface = player_text_font.render("Player 3:", True, (0, 0, 0))
    player3_text_rect = player1_text_surface.get_rect()
    
    player3_text_rect.bottomleft = (10, controls_background_rect.topleft[1] - 150)
    player2_text_rect.bottomleft = (10, player3_text_rect.topleft[1] - 150)
    player1_text_rect.bottomleft = (10, player2_text_rect.topleft[1] - 150)
    
    def create_deck():
        new_deck = [0]
        for i in range(1, 13):
            for _ in range(i):
                new_deck.append(i)
        new_deck.extend(["+2", "+4", "+6", "+8", "+10"])
        return new_deck
    
    deck = create_deck()
    random.shuffle(deck)
    
    
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
    
    hud_rect = pygame.Rect(screen_width // 2 - 180, 15, 360, 46)
    
    def draw_hud(target_surface, state_label, current_round):
        pygame.draw.rect(target_surface, pastel_blue, hud_rect)
        pygame.draw.rect(target_surface, (0, 0, 0), hud_rect, 2)
        state_surface = info_font.render(state_label, True, (0, 0, 0))
        state_rect = state_surface.get_rect()
        state_rect.center = hud_rect.center
        target_surface.blit(state_surface, state_rect)
        round_surface = info_font.render(f"Round: {current_round}", True, (0, 0, 0))
        round_rect = round_surface.get_rect()
        round_rect.midleft = (20, hud_rect.centery)
        target_surface.blit(round_surface, round_rect)
    
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
    
    def wrap_text_lines(text_lines, font, max_width):
        wrapped = []
        for paragraph in text_lines:
            words = paragraph.split()
            current = ""
            for word in words:
                appended = f"{current} {word}".strip()
                if font.size(appended)[0] <= max_width:
                    current = appended
                else:
                    if current:
                        wrapped.append(current)
                    current = word
            if current:
                wrapped.append(current)
            wrapped.append("")
        if wrapped and wrapped[-1] == "":
            wrapped.pop()
        return wrapped
    
    def draw_player_status(target_surface, player, label_rect):
        if not player or not player.status_text:
            return
        status_surface = status_font.render(player.status_text, True, (0, 0, 0))
        status_rect = status_surface.get_rect()
        status_rect.midleft = (label_rect.right + 20, label_rect.centery)
        target_surface.blit(status_surface, status_rect)
    
    def draw_rules_overlay(target_surface):
        overlay_surface = pygame.Surface((rules_overlay_rect.width, rules_overlay_rect.height), pygame.SRCALPHA)
        overlay_surface.fill((0, 0, 0, 210))
        pygame.draw.rect(overlay_surface, (255, 255, 255), overlay_surface.get_rect(), 4)
        margin = 26
        max_width = rules_overlay_rect.width - margin * 2
        wrapped_lines = wrap_text_lines(rules_paragraphs, rules_font, max_width)
        text_y = margin
        line_spacing = rules_font.get_linesize()
        for line in wrapped_lines:
            if not line:
                text_y += line_spacing // 2
                continue
            line_surface = rules_font.render(line, True, (255, 255, 255))
            line_rect = line_surface.get_rect()
            line_rect.centerx = overlay_surface.get_rect().width // 2
            line_rect.y = text_y
            overlay_surface.blit(line_surface, line_rect)
            text_y += line_spacing
        overlay_dest = overlay_surface.get_rect()
        overlay_dest.center = (screen_width // 2, screen_height // 2)
        target_surface.blit(overlay_surface, overlay_dest)
    
    def draw_scoreboard_overlay(target_surface):
        overlay_surface = pygame.Surface((scoreboard_overlay_rect.width, scoreboard_overlay_rect.height), pygame.SRCALPHA)
        overlay_surface.fill((25, 25, 25, 230))
        pygame.draw.rect(overlay_surface, (255, 255, 255), overlay_surface.get_rect(), 4)
        header_surface = scoreboard_font.render("Scoreboard", True, pastel_orange)
        header_rect = header_surface.get_rect()
        header_rect.centerx = overlay_surface.get_rect().width // 2
        header_rect.y = 20
        overlay_surface.blit(header_surface, header_rect)
        text_y = header_rect.bottom + 20
        if not players:
            line_surface = small_score_font.render("Press SPACE to start a round.", True, (255, 255, 255))
            line_rect = line_surface.get_rect()
            line_rect.center = overlay_surface.get_rect().center
            overlay_surface.blit(line_surface, line_rect)
        else:
            for idx, player in enumerate(players, start=1):
                status = "Busted" if player.busted else ("Stayed" if player.stayed else "In play")
                line_text = f"Player {idx}: {player.score} pts | {status}"
                line_surface = small_score_font.render(line_text, True, (255, 255, 255))
                line_rect = line_surface.get_rect()
                line_rect.x = 30
                line_rect.y = text_y
                overlay_surface.blit(line_surface, line_rect)
                text_y += 40
        overlay_dest = overlay_surface.get_rect()
        overlay_dest.center = (screen_width // 2, screen_height // 2)
        target_surface.blit(overlay_surface, overlay_dest)
    
    players = []
    current_player_index = 0
    player_state_labels = ["player 1 turn", "player 2 turn", "player 3 turn"]
    game_over = False
    
    def set_current_player(index):
        nonlocal current_player_index, game_state
        current_player_index = index
        if players:
            players[current_player_index].hit_this_turn = False
        game_state = player_state_labels[index]
    
    def reset_players_for_round():
        for player in players:
            player.hand.clear()
            player.stayed = False
            player.busted = False
            player.hit_this_turn = False
            player.status_text = ""
            player.first_turn_completed = False
            player.round_points_awarded = False
    
    def start_round():
        nonlocal round_number, deck
        if not players:
            return
        round_number += 1
        deck = create_deck()
        random.shuffle(deck)
        reset_players_for_round()
        set_current_player(0)
    
    def all_players_done():
        return players and all(p.stayed or p.busted for p in players)
    
    def advance_to_next_player():
        nonlocal game_state, current_player_index, game_over
        if game_over:
            return
        if not players:
            return
        if all_players_done():
            game_state = "between rounds"
            return
        start_idx = current_player_index
        while True:
            current_player_index = (current_player_index + 1) % len(players)
            next_player = players[current_player_index]
            if not next_player.stayed and not next_player.busted:
                set_current_player(current_player_index)
                break
            if current_player_index == start_idx:
                game_state = "between rounds"
                break
    
    def trigger_game_over():
        nonlocal game_over, game_state
        if not game_over:
            game_over = True
            game_state = "game over"
    
    def check_game_over_condition():
        if game_over or not players:
            return
        for player in players:
            if player.score >= 200:
                trigger_game_over()
                break
    
    def handle_hit(player):
        if not player or player.hit_this_turn or player.stayed or player.busted:
            return
        if not deck:
            return
        new_card = deck.pop()
        already_have = new_card in player.hand
        player.hand.append(new_card)
        if already_have:
            player.busted = True
            player.status_text = f"Busted on {new_card}"
        else:
            player.status_text = f"Hit {new_card}"
        player.hit_this_turn = True
        player.first_turn_completed = True
        advance_to_next_player()
    
    def round_total(player):
        total = 0
        for card in player.hand:
            if isinstance(card, int):
                total += card
            elif isinstance(card, str) and card.startswith("+"):
                total += int(card[1:])
        return total
    
    def award_points_for_player(player):
        if not player or player.round_points_awarded:
            return 0
        points = round_total(player)
        player.score += points
        player.round_points_awarded = True
        check_game_over_condition()
        return points
    
    def handle_stay(player):
        if not player or player.stayed or player.busted:
            return
        if not player.first_turn_completed:
            player.status_text = "Must hit first"
            return
        player.stayed = True
        current_total = round_total(player)
        player.status_text = f"Stayed - {current_total}"
        award_points_for_player(player)
        advance_to_next_player()
    
    player1 = None
    player2 = None
    player3 = None
    
    round_number = 0
    game_state = "title screen"
    rules_visible = False
    scoreboard_visible = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    rules_visible = True
                if event.key == pygame.K_TAB:
                    scoreboard_visible = True
                if game_state == "title screen":
                    if event.key == pygame.K_SPACE:
                        game_state = "between rounds"
                        player1 = Player()
                        player2 = Player()
                        player3 = Player()
                        players = [player1, player2, player3]
                        current_player_index = 0
                elif game_state == "between rounds":
                    if event.key == pygame.K_SPACE:
                        start_round()
                elif game_state in player_state_labels:
                    if not players:
                        continue
                    current_player = players[current_player_index]
                    if event.key == pygame.K_h:
                        handle_hit(current_player)
                    elif event.key == pygame.K_s:
                        handle_stay(current_player)
                
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    rules_visible = False
                if event.key == pygame.K_TAB:
                    scoreboard_visible = False
        
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
            draw_player_status(screen, player1, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            draw_player_status(screen, player2, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
            draw_player_status(screen, player3, player3_text_rect)
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            draw_hud(screen, game_state.replace("_", " ").title(), round_number)
        
        if game_state == "player 1 turn":
            pygame.draw.rect(screen, pastel_red, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(player1_text_surface, player1_text_rect)
            draw_player_status(screen, player1, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            draw_player_status(screen, player2, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
            draw_player_status(screen, player3, player3_text_rect)
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            draw_hud(screen, game_state.replace("_", " ").title(), round_number)
        
        if game_state == "player 2 turn":
            pygame.draw.rect(screen, pastel_green, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(player1_text_surface, player1_text_rect)
            draw_player_status(screen, player1, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            draw_player_status(screen, player2, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
            draw_player_status(screen, player3, player3_text_rect)
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            draw_hud(screen, game_state.replace("_", " ").title(), round_number)
        
        if game_state == "player 3 turn":
            pygame.draw.rect(screen, pastel_blue, background_rect)
            pygame.draw.rect(screen, (0, 0, 0), controls_background_rect)
            screen.blit(controls_surface, controls_text_rect)
            
            screen.blit(player1_text_surface, player1_text_rect)
            draw_player_status(screen, player1, player1_text_rect)
            screen.blit(player2_text_surface, player2_text_rect)
            draw_player_status(screen, player2, player2_text_rect)
            screen.blit(player3_text_surface, player3_text_rect)
            draw_player_status(screen, player3, player3_text_rect)
            draw_player_hand(screen, player1, player1_text_rect, "player1")
            draw_player_hand(screen, player2, player2_text_rect, "player2")
            draw_player_hand(screen, player3, player3_text_rect, "player3")
            
            draw_deck_info(screen)
            draw_hud(screen, game_state.replace("_", " ").title(), round_number)
            
            

        if rules_visible:
            draw_rules_overlay(screen)
        if scoreboard_visible:
            draw_scoreboard_overlay(screen)
        
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
            title_font_size = 160
            subtitle_font_size = 70
            game_over_font = pygame.font.SysFont("Helvetica", title_font_size)
            winner_font = pygame.font.SysFont("Helvetica", subtitle_font_size)
            game_over_surface = game_over_font.render("GAME OVER", True, (0, 0, 0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.center = (screen_width // 2, screen_height // 2 - 80)
            screen.blit(game_over_surface, game_over_rect)
            winner_surface = winner_font.render(f"Player {winner} is the 67 Chungus Queen of Ohio", True, (0, 0, 0))
            winner_rect = winner_surface.get_rect()
            winner_rect.center = (screen_width // 2, screen_height // 2 + 40)
            screen.blit(winner_surface, winner_rect)
            draw_hud(screen, game_state.replace("_", " ").title(), round_number)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()