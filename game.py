import os

import pygame
from typing import Dict, List, Tuple
import time
from state import State
from Games.Arcade.states.title import Title


class Game:
    """The abstract Game player which specific Games will be played on.

    === Public Attributes ===
    width:
        the number of squares wide this board is
    height:
        the number of squares high this board is
    game:
        the game selected to be played
    running:
        whether the game is currently active or not
    player:
        the name of the current player
    """
    # === Private Attributes ===
    # _board:
    #     the board containing the state of the game
    # _surface:
    #     the pygame screen to draw the stage on
    # _icon_map:
    #     the mapping from character (letter) representation to image icons
    # _background_tile:
    #     image icon for the background
    running: bool
    playing: bool
    game_width: int
    game_height: int
    screen_width: int
    screen_height: int
    dt: float
    prev_time = float
    player: str
    states: List[State]
    _screen: pygame.Surface
    _canvas: pygame.Surface
    _icon_map: Dict[chr, pygame.Surface]
    _background_tile: pygame.Surface
    _assets_dir: str
    _sprites_dir: str
    _font_dir: str
    _states_dir: str
    fonts: Dict[int, pygame.font.Font]

    def __init__(self) -> None:
        """Initialize the GameBoard to have dimensions of <width> by <height>.
        """
        pygame.init()
        self.screen_width, self.screen_height = 1920, 1080
        self.game_width, self.game_height = 1280, 720
        self._canvas = pygame.Surface((self.game_width, self.game_height))
        self._screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        pygame.display.set_caption('Arcade: Home')
        self.running = self.playing = True
        self.dt = self.prev_time = 0
        self.load_assets('Arcade')
        self.states = []
        self.actions = {'up': False,
                        'left': False,
                        'down': False,
                        'right': False,
                        'action1': False,
                        'action2': False
                        }
        self.load_state(Title(self))

    def load_state(self, load: State) -> None:
        self.states.append(load)

    def update_resolution(self):
        if self.screen_width == 1920:
            self.screen_width, self.screen_height = 1280, 720
        elif self.screen_width == 1280:
            self.screen_width, self.screen_height = 720, 480
        else:
            self.screen_width, self.screen_height = 1920, 1080
        self._screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

    def game_loop(self) -> None:
        """Main loop for gameplay."""
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = self.playing = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_RETURN or event.key == pygame.K_q:
                    self.actions['action1'] = True
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_e:
                    self.actions['action2'] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_RETURN or event.key == pygame.K_q:
                    self.actions['action1'] = False
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_e:
                    self.actions['action2'] = False

    def update(self) -> None:
        """Update the current state"""
        self.states[-1].update(self.dt, self.actions)

    def render(self) -> None:
        """Render the current content of _canvas onto _screen with
        transformations applied based on the difference between the game
        dimensions and the screen dimensions."""
        self.states[-1].render(self._canvas)
        self._screen.blit(pygame.transform.scale(
            self._canvas, (self.screen_width, self.screen_height)), (0, 0))
        pygame.display.flip()

    def get_dt(self) -> None:
        """Get the amount of time elapsed for the purpose of ensuring
        frame rate independence."""
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface: pygame.Surface,
                  text: str, font_int: int, colour: Tuple[int, int, int],
                  x: int, y: int) -> None:
        """Update <surface> with text rendering reading "<text>" in <colour> at
        coordinates <x>, <y>."""
        rendered_text = self.fonts[font_int].render(text, False, colour)
        # rendered_text.set_colorkey((0, 0, 0))
        text_rect = rendered_text.get_rect()
        text_rect.center = (x, y)
        surface.blit(rendered_text, text_rect)

    def load_assets(self, game: str) -> None:
        """Create pointers to asset folders containing game assets."""
        self._assets_dir = os.path.join('Games', game, 'assets')
        self._sprites_dir = os.path.join(self._assets_dir, 'sprites')
        self._font_dir = os.path.join('Fonts')
        self.fonts = {
            1: pygame.font.Font(os.path.join(self._font_dir, 'ARCADE_I.TTF'), 60),
            2: pygame.font.Font(os.path.join(self._font_dir, 'ARCADE_N.TTF'), 30),
            3: pygame.font.Font(os.path.join(self._font_dir, 'ARCADE_I.TTF'), 30)
        }

    def reset_keys(self) -> None:
        """Set all key presses to False."""
        for action in self.actions:
            self.actions[action] = False

    def reset_action_keys(self):
        self.actions['action1'] = False
        self.actions['action2'] = False
