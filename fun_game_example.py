
"""
fun_game.py

Flip 7 (simplified) demo using pygame.

Rules (this simplified version):
- 2–4 players, all controlled from the same keyboard.
- Each round, every player starts with one card.
- On your turn you may:
    - Hit: draw a card from the deck.
    - Stay: stop drawing for this round and bank the sum of your cards.
- If you ever draw a number you already have in front of you, you bust and
  score 0 this round.
- If you ever reach seven unique numbers in a round, you immediately "Flip 7":
    - The round ends.
    - You score sum(cards) + 15 bonus points.
    - Any other player who has already chosen to Stay keeps their sum;
      everyone else scores 0.
- After each round, scores are added to your total.
- First player to reach 200 or more wins.
"""

import sys
import random
import pygame

# --- Constants ----------------------------------------------------------------

WIDTH, HEIGHT = 900, 600
FPS = 60

BG_COLOR = (20, 20, 30)
PANEL_COLOR = (35, 35, 60)
CARD_COLOR = (230, 230, 255)
CARD_BORDER = (120, 120, 160)
TEXT_COLOR = (240, 240, 255)
HIGHLIGHT_COLOR = (255, 215, 0)
BUST_COLOR = (200, 60, 60)
STAY_COLOR = (80, 200, 120)

TARGET_SCORE = 200
SCORE_FILE = "flip7_scores.txt"


# --- Utility classes ----------------------------------------------------------

class Button:
    """Simple rectangular button with text."""

    def __init__(self, rect, text, font, callback, bg_color=(60, 60, 100)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.callback = callback
        self.bg_color = bg_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=8)
        pygame.draw.rect(surface, CARD_BORDER, self.rect, 2, border_radius=8)
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()


class Deck:
    """Deck of Flip 7 number cards only (no special action cards)."""

    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """Rebuild and shuffle the deck.

        Officially there are 94 cards; this simplified deck uses only numbers:
        1×1, 2×2, ..., 12×12 (78 cards total).
        """
        self.cards = []
        for value in range(1, 13):
            self.cards.extend([value] * value)
        random.shuffle(self.cards)

    def draw(self):
        """Draw a card from the deck, reshuffling automatically if empty."""
        if not self.cards:
            self.reset()
        return self.cards.pop()


# --- Game data structures -----------------------------------------------------

class Player:
    """Represents a single player in the game."""

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.reset_for_round()
        self.total_score = 0

    def reset_for_round(self):
        self.cards = []
        self.card_values = set()
        self.status = "ACTIVE"  # ACTIVE, STAY, BUST
        self.round_score = 0

    def add_card(self, value):
        """Add a card, returning status after the hit: 'OK', 'BUST', or 'FLIP7'."""
        if value in self.card_values:
            self.status = "BUST"
            self.round_score = 0
            return "BUST"
        self.cards.append(value)
        self.card_values.add(value)

        if len(self.card_values) >= 7:
            # Flip 7: immediate end of round, 15 bonus points.
            self.round_score = sum(self.cards) + 15
            self.status = "FLIP7"
            return "FLIP7"

        return "OK"

    def stay(self):
        """Mark player as staying, banking current sum of cards."""
        self.status = "STAY"
        self.round_score = sum(self.cards)

    def apply_round_score(self):
        """Add round score to the total."""
        self.total_score += self.round_score


# --- Game main class ----------------------------------------------------------

class Flip7Game:
    """Main Flip 7 game controller and pygame loop."""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Flip 7 Demo (ENGR 102)")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.font_small = pygame.font.SysFont("arial", 20)
        self.font = pygame.font.SysFont("arial", 28, bold=True)
        self.font_big = pygame.font.SysFont("arial", 40, bold=True)

        self.state = "MENU"  # MENU, RULES, SETUP, PLAYING, ROUND_END, GAME_OVER

        self.buttons = []
        self.deck = Deck()

        self.players = []
        self.current_player_index = 0
        self.num_players = 2

        self.flip7_triggered = False
        self.winner_index = None

        self.last_high_score = self.load_high_score()

        self.create_menu_buttons()

    # --- File I/O -------------------------------------------------------------

    def load_high_score(self):
        """Load the highest score from previous games (file I/O with try/except)."""
        try:
            with open(SCORE_FILE, "r", encoding="utf-8") as f:
                line = f.readline().strip()
                if not line:
                    return None
                parts = line.split(",")
                if len(parts) != 2:
                    return None
                name, score_str = parts
                return {"name": name, "score": int(score_str)}
        except FileNotFoundError:
            return None
        except Exception:
            # File corrupted or unexpected; just ignore.
            return None

    def save_high_score_if_needed(self):
        """Save the best final score to file if it beats the stored high score."""
        best_player = max(self.players, key=lambda p: p.total_score)
        if self.last_high_score is None or best_player.total_score > self.last_high_score["score"]:
            try:
                with open(SCORE_FILE, "w", encoding="utf-8") as f:
                    f.write(f"{best_player.name},{best_player.total_score}\n")
                self.last_high_score = {"name": best_player.name, "score": best_player.total_score}
            except Exception:
                # Silently fail; file I/O is not critical for gameplay.
                pass

    # --- Menu / UI setup ------------------------------------------------------

    def create_menu_buttons(self):
        self.buttons = []

        def start_game():
            self.state = "SETUP"
            self.buttons = []  # Rebuild in setup state.

        def show_rules():
            self.state = "RULES"
            self.create_rules_buttons()

        def quit_game():
            pygame.quit()
            sys.exit()

        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 100, 260, 200, 50),
                text="Play Flip 7",
                font=self.font,
                callback=start_game,
            )
        )
        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 100, 330, 200, 50),
                text="Rules",
                font=self.font,
                callback=show_rules,
            )
        )
        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 100, 400, 200, 50),
                text="Quit",
                font=self.font,
                callback=quit_game,
            )
        )

    def create_rules_buttons(self):
        self.buttons = []

        def back_to_menu():
            self.state = "MENU"
            self.create_menu_buttons()

        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 80, HEIGHT - 80, 160, 40),
                text="Back to Menu",
                font=self.font,
                callback=back_to_menu,
            )
        )

    def create_setup_buttons(self):
        self.buttons = []

        def set_players(n):
            self.num_players = n

        def start():
            self.start_new_game()

        def back_to_menu():
            self.state = "MENU"
            self.create_menu_buttons()

        x_start = WIDTH // 2 - 180
        for i, n in enumerate([2, 3, 4]):
            self.buttons.append(
                Button(
                    rect=(x_start + i * 120, 260, 100, 50),
                    text=f"{n} Players",
                    font=self.font_small,
                    callback=lambda n=n: set_players(n),
                )
            )

        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 100, 340, 200, 50),
                text="Start Game",
                font=self.font,
                callback=start,
            )
        )
        self.buttons.append(
            Button(
                rect=(WIDTH // 2 - 100, 410, 200, 50),
                text="Back",
                font=self.font,
                callback=back_to_menu,
            )
        )

    # --- Game lifecycle -------------------------------------------------------

    def start_new_game(self):
        """Initialize players and start the first round."""
        self.players = []
        colors = [
            (80, 160, 255),
            (255, 140, 0),
            (140, 220, 140),
            (255, 120, 200),
        ]
        for i in range(self.num_players):
            player = Player(f"Player {i + 1}", colors[i % len(colors)])
            self.players.append(player)

        self.deck.reset()
        self.start_new_round()
        self.state = "PLAYING"

    def start_new_round(self):
        """Prepare players and deck for a new round."""
        self.flip7_triggered = False
        for player in self.players:
            player.reset_for_round()
            # Initial card
            value = self.deck.draw()
            player.add_card(value)
            # Initial card cannot bust or flip 7 in this simplified variant.

        self.current_player_index = 0
        self.advance_to_next_active_player_if_needed()

    def advance_to_next_active_player_if_needed(self):
        """Move current_player_index to the next ACTIVE player, if any."""
        active_indices = [i for i, p in enumerate(self.players) if p.status == "ACTIVE"]
        if not active_indices:
            # End of round
            self.resolve_round()
            return

        # If current is not active, move to the next active index.
        if self.players[self.current_player_index].status != "ACTIVE":
            # Simple rotation through players with a loop.
            for offset in range(1, len(self.players) + 1):
                idx = (self.current_player_index + offset) % len(self.players)
                if self.players[idx].status == "ACTIVE":
                    self.current_player_index = idx
                    break

    def resolve_round(self):
        """Apply round scores, check for winner, and move to ROUND_END or GAME_OVER."""
        # For non-Flip7 rounds, compute scores now.
        if not self.flip7_triggered:
            for player in self.players:
                if player.status == "STAY":
                    player.round_score = sum(player.cards)
                elif player.status == "BUST":
                    player.round_score = 0
                elif player.status == "ACTIVE":
                    # They neither stayed nor busted, so they get nothing.
                    player.round_score = 0
        # If Flip 7 triggered, scores were already assigned in add_card and stay().

        # Add to totals.
        for player in self.players:
            player.apply_round_score()

        # Check if someone reached or exceeded target score.
        best = max(self.players, key=lambda p: p.total_score)
        if best.total_score >= TARGET_SCORE:
            self.winner_index = self.players.index(best)
            self.save_high_score_if_needed()
            self.state = "GAME_OVER"
        else:
            self.state = "ROUND_END"

    def handle_hit(self):
        """Handle 'Hit' action for the current player."""
        if self.state != "PLAYING":
            return
        player = self.players[self.current_player_index]
        if player.status != "ACTIVE":
            return
        value = self.deck.draw()
        status = player.add_card(value)
        if status == "BUST":
            # Move to next player if possible.
            self.advance_to_next_active_player_if_needed()
        elif status == "FLIP7":
            # End round immediately.
            self.flip7_triggered = True
            # Everyone who stayed keeps their round_score; active players get 0.
            for p in self.players:
                if p is player:
                    # round_score already set with +15 bonus.
                    continue
                if p.status == "STAY":
                    p.round_score = sum(p.cards)
                else:
                    p.status = "BUST"
                    p.round_score = 0
            self.resolve_round()
        # status == 'OK': same player continues; no index change.

    def handle_stay(self):
        """Handle 'Stay' action for the current player."""
        if self.state != "PLAYING":
            return
        player = self.players[self.current_player_index]
        if player.status != "ACTIVE":
            return
        player.stay()
        self.advance_to_next_active_player_if_needed()

    def handle_next_round(self):
        """Transition from ROUND_END to PLAYING after key press."""
        if self.state == "ROUND_END":
            self.start_new_round()
            self.state = "PLAYING"

    def handle_quit_to_menu(self):
        """Allow user to quit early back to menu from within game."""
        self.state = "MENU"
        self.create_menu_buttons()

    # --- Drawing helpers ------------------------------------------------------

    def draw_text(self, text, x, y, font=None, color=TEXT_COLOR, center=False):
        if font is None:
            font = self.font_small
        surf = font.render(text, True, color)
        rect = surf.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        self.screen.blit(surf, rect)

    def draw_menu(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("Flip 7 Demo", WIDTH // 2, 120, font=self.font_big, color=HIGHLIGHT_COLOR, center=True)
        self.draw_text(
            "Press-your-luck card game. First to 200 points wins.",
            WIDTH // 2,
            170,
            font=self.font_small,
            color=TEXT_COLOR,
            center=True,
        )

        if self.last_high_score:
            self.draw_text(
                f"High Score: {self.last_high_score['name']} ({self.last_high_score['score']})",
                WIDTH // 2,
                210,
                font=self.font_small,
                color=(180, 180, 220),
                center=True,
            )

        for btn in self.buttons:
            btn.draw(self.screen)

    def draw_rules(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("Flip 7 - Simplified Rules", WIDTH // 2, 60, font=self.font_big, color=HIGHLIGHT_COLOR, center=True)

        rules_lines = [
            "Goal: Be the first player to reach 200 points.",
            "",
            "On your turn:",
            "  - Hit: draw a card. If you draw a number you already have, you bust.",
            "  - Stay: stop drawing and bank the sum of your cards for this round.",
            "",
            "Flip 7 bonus:",
            "  If you ever have 7 unique numbers, the round ends immediately.",
            "  You score sum(cards) + 15 bonus points.",
            "",
            "Round end:",
            "  Players who stayed score the sum of their cards.",
            "  Players who busted or never stayed score 0.",
            "",
            "Controls in game:",
            "  H = Hit, S = Stay, ESC = Quit to menu.",
            "  R = Show rules overlay, SPACE = next round (after it ends).",
        ]

        y = 110
        for line in rules_lines:
            self.draw_text(line, 80, y, font=self.font_small, color=TEXT_COLOR)
            y += 26

        for btn in self.buttons:
            btn.draw(self.screen)

    def draw_setup(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("New Game Setup", WIDTH // 2, 120, font=self.font_big, color=HIGHLIGHT_COLOR, center=True)
        self.draw_text("Choose number of players (2–4) and click Start Game.", WIDTH // 2, 170,
                       font=self.font_small, color=TEXT_COLOR, center=True)
        self.draw_text(f"Selected: {self.num_players} players", WIDTH // 2, 210,
                       font=self.font, color=(200, 200, 255), center=True)

        for btn in self.buttons:
            btn.draw(self.screen)

    def draw_cards_for_player(self, player, x, y):
        """Draw a row of card rectangles showing this player's cards."""
        spacing = 60
        card_w, card_h = 50, 80
        for i, value in enumerate(player.cards):
            rect = pygame.Rect(x + i * spacing, y, card_w, card_h)
            color = CARD_COLOR
            pygame.draw.rect(self.screen, color, rect, border_radius=6)
            pygame.draw.rect(self.screen, CARD_BORDER, rect, 2, border_radius=6)
            self.draw_text(str(value), rect.centerx, rect.centery - 8, font=self.font, color=(0, 0, 0), center=True)

    def draw_playing(self):
        self.screen.fill(BG_COLOR)

        # Top info bar
        pygame.draw.rect(self.screen, PANEL_COLOR, (0, 0, WIDTH, 80))
        self.draw_text("Flip 7 Demo", 20, 20, font=self.font_big, color=HIGHLIGHT_COLOR)
        self.draw_text(f"Target Score: {TARGET_SCORE}", WIDTH - 260, 20, font=self.font_small)

        current = self.players[self.current_player_index]
        self.draw_text(f"Current Turn: {current.name}", 20, 50, font=self.font)

        # Instructions
        self.draw_text("Controls: [H]it  [S]tay  [R]ules overlay  [ESC] Quit to menu", 20, 90, font=self.font_small)

        # Player panels
        panel_top = 120
        panel_height = (HEIGHT - panel_top - 40) // len(self.players)
        for i, player in enumerate(self.players):
            top = panel_top + i * panel_height
            pygame.draw.rect(self.screen, PANEL_COLOR, (20, top, WIDTH - 40, panel_height - 10), border_radius=12)
            name_color = player.color

            status_text = player.status
            status_color = TEXT_COLOR
            if player.status == "BUST":
                status_color = BUST_COLOR
            elif player.status in ("STAY", "FLIP7"):
                status_color = STAY_COLOR

            self.draw_text(player.name, 40, top + 10, font=self.font, color=name_color)
            self.draw_text(f"Total: {player.total_score}", WIDTH - 220, top + 10, font=self.font_small)
            self.draw_text(f"Round: {player.round_score}", WIDTH - 120, top + 10, font=self.font_small)

            self.draw_text(f"Status: {status_text}", 40, top + 45, font=self.font_small, color=status_color)
            self.draw_cards_for_player(player, x=40, y=top + 75)

        # If round is effectively over but we haven't transitioned yet, show hint.
        active = any(p.status == "ACTIVE" for p in self.players)
        if not active:
            self.draw_text("All players are done. Press SPACE to continue.", WIDTH // 2, HEIGHT - 40,
                           font=self.font_small, color=HIGHLIGHT_COLOR, center=True)

    def draw_round_end(self):
        self.screen.fill(BG_COLOR)
        self.draw_text("Round Over", WIDTH // 2, 60, font=self.font_big, color=HIGHLIGHT_COLOR, center=True)

        y = 120
        for player in self.players:
            color = player.color
            text = f"{player.name}: +{player.round_score} this round (Total: {player.total_score})"
            self.draw_text(text, 80, y, font=self.font, color=color)
            y += 50

        self.draw_text("Press SPACE to begin the next round.", WIDTH // 2, HEIGHT - 80,
                       font=self.font, color=TEXT_COLOR, center=True)
        self.draw_text("Press ESC to quit early to menu.", WIDTH // 2, HEIGHT - 50,
                       font=self.font_small, color=TEXT_COLOR, center=True)

    def draw_game_over(self):
        self.screen.fill(BG_COLOR)
        winner = self.players[self.winner_index]
        self.draw_text("Game Over", WIDTH // 2, 80, font=self.font_big, color=HIGHLIGHT_COLOR, center=True)
        self.draw_text(f"Winner: {winner.name} ({winner.total_score} points)",
                       WIDTH // 2, 150, font=self.font, color=winner.color, center=True)

        y = 210
        for player in self.players:
            self.draw_text(f"{player.name} - {player.total_score} pts", WIDTH // 2, y,
                           font=self.font_small, color=player.color, center=True)
            y += 35

        if self.last_high_score:
            self.draw_text(
                f"High Score: {self.last_high_score['name']} ({self.last_high_score['score']})",
                WIDTH // 2, y + 20,
                font=self.font_small, color=(200, 200, 255), center=True,
            )

        self.draw_text("Press ENTER to return to menu.", WIDTH // 2, HEIGHT - 80,
                       font=self.font, color=TEXT_COLOR, center=True)
        self.draw_text("Press ESC to quit.", WIDTH // 2, HEIGHT - 50,
                       font=self.font_small, color=TEXT_COLOR, center=True)

    # --- Event handling -------------------------------------------------------

    def handle_events(self):
        """Process pygame events for the current state."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.state in ("MENU", "RULES", "SETUP"):
                for btn in self.buttons:
                    btn.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if self.state == "PLAYING":
                    if event.key == pygame.K_h:
                        self.handle_hit()
                    elif event.key == pygame.K_s:
                        self.handle_stay()
                    elif event.key == pygame.K_SPACE:
                        # Let SPACE advance from implicit round end.
                        active = any(p.status == "ACTIVE" for p in self.players)
                        if not active:
                            self.resolve_round()
                    elif event.key == pygame.K_r:
                        # Quick rules overlay: just toggle to RULES and back.
                        self.state = "RULES"
                        self.create_rules_buttons()
                    elif event.key == pygame.K_ESCAPE:
                        self.handle_quit_to_menu()

                elif self.state == "ROUND_END":
                    if event.key == pygame.K_SPACE:
                        self.handle_next_round()
                    elif event.key == pygame.K_ESCAPE:
                        self.handle_quit_to_menu()

                elif self.state == "GAME_OVER":
                    if event.key == pygame.K_RETURN:
                        self.state = "MENU"
                        self.create_menu_buttons()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                elif self.state == "SETUP":
                    if event.key == pygame.K_2:
                        self.num_players = 2
                    elif event.key == pygame.K_3:
                        self.num_players = 3
                    elif event.key == pygame.K_4:
                        self.num_players = 4
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "MENU"
                        self.create_menu_buttons()

                elif self.state == "RULES":
                    if event.key == pygame.K_ESCAPE:
                        self.state = "MENU"
                        self.create_menu_buttons()

    # --- Main loop ------------------------------------------------------------

    def run(self):
        """Primary pygame loop."""
        while True:
            self.clock.tick(FPS)
            self.handle_events()

            if self.state == "MENU":
                self.draw_menu()
            elif self.state == "RULES":
                self.draw_rules()
            elif self.state == "SETUP":
                if not self.buttons:
                    self.create_setup_buttons()
                self.draw_setup()
            elif self.state == "PLAYING":
                self.draw_playing()
            elif self.state == "ROUND_END":
                self.draw_round_end()
            elif self.state == "GAME_OVER":
                self.draw_game_over()

            pygame.display.flip()


def main():
    """Entry point."""
    game = Flip7Game()
    game.run()


if __name__ == "__main__":
    main()
