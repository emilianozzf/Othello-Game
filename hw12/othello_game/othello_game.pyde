from game_controller import GameController
from board import Board
from player1 import Player1
from player2 import Player2


WIDTH = 800
HEIGHT = 800
time_delay_counter = 120

game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, game_controller)
player1 = Player1(board, game_controller)
player2 = Player2(board, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    global time_delay_counter

    background(0, 0.35, 0)
    board.display()
    game_controller.update()
    if (not game_controller.game_over) and (not game_controller.player1_turn):
        time_delay_counter -= 1
        if time_delay_counter == 0:
            player2.move()
            time_delay_counter = 120


def mousePressed():
    if (not game_controller.game_over) and (game_controller.player1_turn):
        player1.move(mouseX, mouseY)
