from __future__ import annotations
from typing import Optional


class State:
    """A State which the Player can interact with. States can be held in memory
    while the Player interacts with another state. States are held in a stack in
    the Game class.

    === Public Attributes ===
    game:
        the Game object which is currently being played by the Player
    prev_state:
        the previous State (prior to the current one), will resume when the
        current state is concluded
    """
    prev_state: Optional[State]

    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, delta_time, actions):
        raise NotImplementedError

    def render(self, surface):
        raise NotImplementedError

    def enter_state(self):
        if len(self.game.states) > 1:
            self.prev_state = self.game.states[-1]
        self.game.states.append(self)

    def exit_state(self):
        self.game.states.pop()
