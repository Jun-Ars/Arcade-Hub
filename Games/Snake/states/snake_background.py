from state import State
import pygame


class Snake_Background(State):

    def __init__(self, game):
        State.__init__(self, game)
        self.snake = Snake(self.game)

    def update(self, delta_time, actions) -> None:
        self.snake.update(delta_time, actions)

    def render(self, surface) -> None:
        surface.fill((66, 245, 105))
        self.snake.render(surface)
        self.game.draw_text(surface,
                            "...pretend the snake keeps running", 2, (0, 0, 0),
                            self.game.game_width // 2,
                            self.game.game_height // 2)
        self.game.draw_text(surface,
                            "even when you let go of the button", 2,
                            (0, 0, 0),
                            self.game.game_width // 2,
                            self.game.game_height // 2 + 30)
        self.game.draw_text(surface, 'SCORE: 0', 2, (0, 0, 0), self.game.game_width * 0.1, 20)


class Snake():
    def __init__(self, game) -> None:
        self.game = game
        self.position_x, self.position_y = self.game.game_width // 2, self.game.game_height // 2
        self.current_frame, self.last_frame_update = 0, 0

    def update(self, delta_time, actions):
        direction_x = actions['right'] - actions['left']
        direction_y = actions['down'] - actions['up']
        self.position_x += 300 * delta_time * direction_x
        self.position_y += 300 * delta_time * direction_y

        self.animate(delta_time, direction_x, direction_y)

    def render(self, display):
        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(self.position_x, self.position_y, 50, 50))

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
