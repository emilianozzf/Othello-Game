from game_controller import GameController
from board import Board
from player1 import Player1
from player2 import Player2


WIDTH = 400
HEIGHT = 400


game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, game_controller)
player1 = Player1(board, game_controller)
player2 = Player2(board, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(0, 0.35, 0)
    board.display()
    game_controller.update()


def mousePressed():
    if game_controller.player1_turn:
        player1.move(mouseX, mouseY)
    else:
        player2.move(mouseX, mouseY)
