from state import State
import pygame


class TetrisMain(State):

    def __init__(self, game):
        State.__init__(self, game)
        self.tetrimino = Tetrimino(self.game)

    def update(self, delta_time, actions) -> None:
        self.tetrimino.update(delta_time, actions)

    def render(self, surface) -> None:
        surface.fill((66, 245, 105))
        self.tetrimino.render(surface)
        self.game.draw_text(surface,
                            "COMING SOON!", 2, (0, 0, 0),
                            self.game.game_width // 2,
                            self.game.game_height // 2)
        self.game.draw_text(surface,
                            "SHOULDNT BE LONG!", 2,
                            (0, 0, 0),
                            self.game.game_width // 2,
                            self.game.game_height // 2 + 30)
        self.game.draw_text(surface, 'SCORE: 0', 2, (0, 0, 0), self.game.game_width * 0.1, 20)


class Tetrimino():
    def __init__(self, game) -> None:
        self.game = game
        self._last_frame_update = 0
        self.position_x, self.position_y = self.game.game_width // 2, self.game.game_height // 2
        self.current_frame, self.last_frame_update = 0, 0
        self.cur_fill = 0
        self.filled = {
            0: [[0, 1, 0], [1, 1, 1], [0, 0, 0]],
            1: [[0, 1, 0], [0, 1, 1], [0, 1, 0]],
            2: [[0, 0, 0], [1, 1, 1], [0, 1, 0]],
            3: [[0, 1, 0], [1, 1, 0], [0, 1, 0]]
        }

    def update(self, delta_time, actions):
        direction_x = actions['right'] - actions['left']
        direction_y = actions['down'] - actions['up']
        if actions['action1']:
            self.rotate()
            self.game.reset_action_keys()
        if actions['action2']:
            self.rotate(-1)
            self.game.reset_action_keys()

        self.position_x += 300 * delta_time * direction_x
        self.position_y += 300 * delta_time * direction_y

        self.animate(delta_time, direction_x, direction_y)

    def render(self, display):
        for row, r_fill in enumerate(self.filled[self.cur_fill]):
            for column, c_fill in enumerate(self.filled[self.cur_fill][row]):
                if r_fill and c_fill:
                    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(self.position_x + 50 * column, self.position_y + 50 * row, 50, 50))

    def rotate(self, rev: int = 1):
        self.cur_fill = (self.cur_fill + rev) % 4

    def animate(self, delta_time, direction_x, direction_y):

        # Compute how much time has passed since the frame last updated
        # self.last_frame_update += delta_time
        # If no direction is pressed, set image to idle and return
        # if not (direction_x or direction_y):
        #     self.curr_image = self.curr_anim_list[0]
        #     return
        # If an image was pressed, use the appropriate list of frames according to direction
        # if direction_x:
        #     if direction_x > 0:
        #         self.curr_anim_list = self.right_sprites
        #     else:
        #         self.curr_anim_list = self.left_sprites
        # if direction_y:
        #     if direction_y > 0:
        #         self.curr_anim_list = self.front_sprites
        #     else:
        #         self.curr_anim_list = self.back_sprites
        # Advance the animation if enough time has elapsed
        # if self.last_frame_update > .15:
        #     self.last_frame_update = 0
        #     self.current_frame = (self.current_frame + 1) % len(
        #         self.curr_anim_list)
        #     self.curr_image = self.curr_anim_list[self.current_frame]
            pass
