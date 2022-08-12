from typing import List, Tuple
from state import State
from Fonts.font_config import COLOURS, SPACING


class Title(State):
    """Main title screen for choosing a game or changing options."""
    _last_frame_update: float

    def __init__(self, game):
        State.__init__(self, game)
        self.index = 0

        self.cursor_colour = COLOURS['MENU']
        self.menu_options = {
            0: 'PLAY GAME',
            1: 'OPTIONS',
            2: 'QUIT'
        }
        self._flash = 0
        self._last_frame_update = 0

    def reset_menu_options(self, new_menu_options: List[str]) -> None:
        self.menu_options = {}
        new_menu_options.append('BACK')
        for i, menu_option in enumerate(new_menu_options):
            self.menu_options[i] = menu_option

    def update(self, delta_time, actions) -> None:
        self.update_cursor(actions)
        self.cursor_colour = self.animate_cursor(delta_time)
        if actions['action1']:
            self.transition_state()
        self.game.reset_keys()

    def render(self, surface) -> None:
        surface.fill(COLOURS['BG'])
        # Draw the menu screen
        self.game.draw_text(
            surface, "ARCADE MAIN MENU", 1, COLOURS['MENU'],
            self.game.game_width // 2, self.game.game_height // 2 - 100)
        # Draw meny options
        for item in self.menu_options:
            self.game.draw_text(
                surface, self.menu_options[item], 2, COLOURS['MENU'],
                self.game.game_width // 2,
                self.game.game_height // 2 + SPACING['MENU'] * item
            )
        # Draw currently selected menu option
        self.game.draw_text(
            surface, self.menu_options[self.index], 2, self.cursor_colour,
            self.game.game_width // 2,
            self.game.game_height // 2 + SPACING['MENU'] * self.index
        )

    def update_cursor(self, actions) -> None:
        if actions['down'] or actions['up']:
            if actions['down']:
                self.index = (self.index + 1) % len(self.menu_options)
            else:
                self.index = (self.index - 1) % len(self.menu_options)
            self._flash = 1
            self._last_frame_update = 0

    def animate_cursor(self, delta_time) -> Tuple[int, int, int]:
        self._last_frame_update += delta_time
        if self._last_frame_update > 0.5:
            self._last_frame_update = 0
            self._flash = (self._flash + 1) % 2
        if self._flash:
            return COLOURS['SELECTION']
        else:
            return COLOURS['MENU']

    def transition_state(self) -> None:
        if self.menu_options[self.index] == 'PLAY GAME':
            from Games.Arcade.states.game_picker import GamePicker
            new_state = GamePicker(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == 'OPTIONS':
            from Games.Arcade.states.options import Options
            new_state = Options(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == 'QUIT':
            self.game.running = self.game.playing = False

