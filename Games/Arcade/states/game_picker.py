import os

from Games.Arcade.states.title import Title


class GamePicker(Title):
    """Arcade Meny for choosing a game."""

    def __init__(self, game):
        Title.__init__(self, game)
        games_list = os.listdir(os.path.join('Games'))
        games_list.remove('Arcade')
        self.reset_menu_options(games_list)

    def transition_state(self) -> None:
        if self.menu_options[self.index] == 'Snake':
            from Games.Snake.states.snake_background import Snake_Background
            new_state = Snake_Background(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == 'Tetris':
            from Games.Tetris.states.tetris_main import TetrisMain
            new_state = TetrisMain(self.game)
            new_state.enter_state()
        elif self.menu_options[self.index] == 'BACK':
            self.exit_state()
