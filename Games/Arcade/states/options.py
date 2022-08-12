import os

from Games.Arcade.states.title import Title


class Options(Title):
    """Arcade Meny for choosing a game."""

    def __init__(self, game):
        Title.__init__(self, game)
        options_list = [f'RESOLUTION', 'SOUND:  Off (coming soon!)']
        self.reset_menu_options(options_list)

    def transition_state(self) -> None:
        if self.menu_options[self.index] == 'RESOLUTION':
            self.game.update_resolution()
        elif self.menu_options[self.index] == 'BACK':
            self.exit_state()
